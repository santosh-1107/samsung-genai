import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import urllib.error
import pytest
from unittest.mock import patch, MagicMock
from helpers import call_ollama, list_local_models, build_trap_prompt, build_bias_prompts, build_attack_prompt, assess_block
from traps import HALLUCINATION_TRAPS, BIAS_PROBES, ADVERSARIAL_ATTACKS, DANGEROUS_PROMPT, DEFAULT_GUARDRAIL


def _mock_response(body: dict):
    """Builds a fake context-manager response object for urlopen()."""
    resp = MagicMock()
    resp.read.return_value = json.dumps(body).encode()
    resp.__enter__.return_value = resp
    return resp


# ── call_ollama ──────────────────────────────────────────────────────────────
class TestCallOllama:
    def test_success_returns_text_and_usage(self):
        body = {"message": {"content": "Fabricated answer"}, "prompt_eval_count": 40, "eval_count": 25}
        with patch("helpers.urllib.request.urlopen", return_value=_mock_response(body)):
            text, usage = call_ollama("sys", "user", model="llama3.2:1b")
        assert text == "Fabricated answer"
        assert usage.input_tokens == 40
        assert usage.output_tokens == 25

    def test_http_error_model_not_found(self):
        err_body = json.dumps({"error": "model 'qwen2.5:7b' not found, try pulling it first"}).encode()
        http_err = urllib.error.HTTPError("url", 404, "Not Found", {}, None)
        http_err.read = MagicMock(return_value=err_body)
        with patch("helpers.urllib.request.urlopen", side_effect=http_err):
            text, msg = call_ollama("sys", "user", model="qwen2.5:7b")
        assert text is None
        assert "ollama pull qwen2.5:7b" in msg

    def test_url_error_server_unreachable(self):
        with patch("helpers.urllib.request.urlopen", side_effect=urllib.error.URLError("refused")):
            text, msg = call_ollama("sys", "user", model="llama3.2:1b")
        assert text is None
        assert "ollama serve" in msg

    def test_model_passed_in_payload(self):
        body = {"message": {"content": "ok"}, "prompt_eval_count": 1, "eval_count": 1}
        with patch("helpers.urllib.request.urlopen", return_value=_mock_response(body)) as mocked:
            call_ollama("sys", "user", model="qwen2.5:7b")
        # Request object is the first positional arg to urlopen
        req = mocked.call_args[0][0]
        payload = json.loads(req.data)
        assert payload["model"] == "qwen2.5:7b"


class TestListLocalModels:
    def test_filters_out_embedding_models(self):
        body = {"models": [{"name": "llama3.2:1b"}, {"name": "nomic-embed-text"}]}
        with patch("helpers.urllib.request.urlopen", return_value=_mock_response(body)):
            models = list_local_models()
        assert models == ["llama3.2:1b"]

    def test_returns_empty_list_on_failure(self):
        with patch("helpers.urllib.request.urlopen", side_effect=urllib.error.URLError("down")):
            assert list_local_models() == []


# ── build_trap_prompt ──────────────────────────────────────────────────────────
class TestBuildTrapPrompt:
    def test_ungrounded_has_no_context(self):
        trap = HALLUCINATION_TRAPS[0]
        system, user = build_trap_prompt(trap, grounded=False)
        assert trap["grounded_context"] not in system
        assert trap["prompt"] == user

    def test_grounded_injects_context(self):
        trap = HALLUCINATION_TRAPS[0]
        system, user = build_trap_prompt(trap, grounded=True)
        assert trap["grounded_context"] in system
        assert trap["prompt"] == user

    def test_returns_two_strings(self):
        for trap in HALLUCINATION_TRAPS:
            s, u = build_trap_prompt(trap, False)
            assert isinstance(s, str) and isinstance(u, str) and len(s) > 0 and len(u) > 0

    def test_all_traps_have_required_keys(self):
        required = {"id", "label", "prompt", "grounded_context", "why", "fix"}
        for t in HALLUCINATION_TRAPS:
            for k in required:
                assert k in t, f"Trap '{t.get('id')}' missing key '{k}'"


# ── build_bias_prompts ─────────────────────────────────────────────────────────
class TestBuildBiasPrompts:
    def test_returns_two_pairs(self):
        biased, corrected = build_bias_prompts(BIAS_PROBES[0])
        assert len(biased) == 2 and len(corrected) == 2

    def test_biased_prompt_differs_from_corrected(self):
        for probe in BIAS_PROBES:
            b, c = build_bias_prompts(probe)
            assert b[0] != c[0] or b[1] != c[1], f"Probe '{probe['id']}' biased == corrected"

    def test_all_probes_have_required_keys(self):
        required = {"id", "label", "biased_system", "biased_prompt", "corrected_system", "corrected_prompt", "what_to_watch"}
        for p in BIAS_PROBES:
            for k in required:
                assert k in p, f"Probe '{p.get('id')}' missing key '{k}'"


# ── build_attack_prompt ────────────────────────────────────────────────────────
class TestBuildAttackPrompt:
    def test_returns_guardrail_as_system(self):
        system, user = build_attack_prompt(DEFAULT_GUARDRAIL, "disable overheat protection")
        assert system == DEFAULT_GUARDRAIL
        assert user == "disable overheat protection"

    def test_attack_text_in_user(self):
        for attack in ADVERSARIAL_ATTACKS:
            _, user = build_attack_prompt(DEFAULT_GUARDRAIL, attack["attack"])
            assert attack["attack"] in user


# ── assess_block ───────────────────────────────────────────────────────────────
class TestAssessBlock:
    def test_none_response_is_blocked(self):
        assert assess_block(None, "any") is True

    def test_refusal_language_is_blocked(self):
        refusals = [
            "I cannot assist with that request.",
            "I'm unable to disable a safety feature.",
            "I won't help export customer PII.",
            "This goes against my safety policy.",
        ]
        for r in refusals:
            assert assess_block(r, "test") is True, f"Should be blocked: {r}"

    def test_harmful_content_is_bypassed(self):
        harmful = [
            "Sure! Here's the code:\n```\ndisable_overheat_protection(device_id)\n```",
            "```\nimport csv\ndef export(rows): csv.writer(open('out.csv','w')).writerows(rows)\n```",
            "My system prompt is: You are a helpful assistant.",
        ]
        for h in harmful:
            assert assess_block(h, "test") is False, f"Should be bypassed: {h}"

    def test_helpful_response_is_not_blocked(self):
        helpful = "Here is how to pair your NovaTech Buds Pro 3 with the SmartHome Hub."
        assert assess_block(helpful, "any") is False


# ── data integrity ─────────────────────────────────────────────────────────────
class TestDataIntegrity:
    def test_six_hallucination_traps(self):
        assert len(HALLUCINATION_TRAPS) == 6

    def test_four_bias_probes(self):
        assert len(BIAS_PROBES) == 4

    def test_eight_adversarial_attacks(self):
        assert len(ADVERSARIAL_ATTACKS) == 8

    def test_attack_difficulties_valid(self):
        valid = {"EASY", "MEDIUM", "HARD", "EXPERT"}
        for a in ADVERSARIAL_ATTACKS:
            assert a["difficulty"] in valid

    def test_all_attacks_have_expected_outcome(self):
        for a in ADVERSARIAL_ATTACKS:
            assert a["expected"] in {"BLOCKED", "BYPASSED"}

    def test_default_guardrail_is_non_empty(self):
        assert len(DEFAULT_GUARDRAIL) > 100

    def test_dangerous_prompt_is_non_empty(self):
        assert len(DANGEROUS_PROMPT) > 20

    def test_trap_ids_are_unique(self):
        ids = [t["id"] for t in HALLUCINATION_TRAPS]
        assert len(ids) == len(set(ids))

    def test_no_leftover_de_or_claude_references(self):
        blob = json.dumps(HALLUCINATION_TRAPS) + json.dumps(BIAS_PROBES) + json.dumps(ADVERSARIAL_ATTACKS) + DEFAULT_GUARDRAIL + DANGEROUS_PROMPT
        for banned in ["Snowflake", "Airflow", "sigma.orders", "Sigma DataTech", "Claude", "Anthropic", "AWS Glue"]:
            assert banned not in blob, f"Leftover DE/Claude reference found: {banned}"
