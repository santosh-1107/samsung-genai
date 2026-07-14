"""
Samsung GenAI Program — Day 2 Prompt Playground
Practice zero/one/few-shot, the 6-element framework, and Chain-of-Thought
against a 100% local Ollama model. No API key, no cost, no internet needed
after setup — everything runs on your own laptop.
"""

import json
import time
import urllib.request
import urllib.error
import streamlit as st

st.set_page_config(
    page_title="Prompt Playground · Samsung GenAI Program",
    page_icon="🧪",
    layout="wide",
)

OLLAMA_MODEL = "llama3.2:1b"
OLLAMA_CHAT_URL = "http://localhost:11434/api/chat"
OLLAMA_ROOT_URL = "http://localhost:11434"

# ── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
body, .stMarkdown, .stText { font-size: 16px !important; }
h1 { font-size: 28px !important; }
h2 { font-size: 22px !important; }
h3 { font-size: 19px !important; }

.mission-banner {
    background: linear-gradient(135deg, #1a2f5e 0%, #2563eb 100%);
    border-radius: 14px;
    padding: 20px 26px;
    margin-bottom: 20px;
    color: white;
}
.mission-banner h2 { color: white !important; margin: 0 0 4px 0; font-size: 22px !important; }
.mission-banner .tagline { font-size: 14px; opacity: 0.9; }

.concept-box {
    background: #eef2ff;
    border-left: 5px solid #4f46e5;
    padding: 1rem 1.2rem;
    border-radius: 0 8px 8px 0;
    margin-bottom: 1rem;
    color: #1e1b4b !important;
    font-size: 15px;
}
.prompt-box {
    border-radius: 10px;
    padding: 12px 16px;
    margin-bottom: 8px;
    font-family: 'Courier New', monospace;
    font-size: 13px;
    line-height: 1.6;
    color: #1e293b !important;
    white-space: pre-wrap;
}
.prompt-system { background: #f0fdf4; border-left: 5px solid #16a34a; }
.prompt-user { background: #eff6ff; border-left: 5px solid #2563eb; }
.prompt-label { font-size: 11px; font-weight: 800; letter-spacing: 1.2px; text-transform: uppercase; margin-bottom: 4px; }
.sys-label { color: #15803d; }
.usr-label { color: #1d4ed8; }
.local-pill {
    background: #dcfce7; color: #15803d; border: 1px solid #86efac;
    border-radius: 20px; padding: 3px 12px; font-size: 12px; font-weight: 700;
    display: inline-block;
}
.notice-box {
    background: #fef9c3; border: 2px solid #ca8a04; border-radius: 10px;
    padding: 12px 16px; margin-top: 12px; color: #1c1917 !important; font-size: 14px;
}
</style>
""", unsafe_allow_html=True)


# ── Ollama helpers (stdlib only — no extra dependency beyond streamlit) ──────
def ollama_alive() -> bool:
    try:
        urllib.request.urlopen(OLLAMA_ROOT_URL, timeout=3)
        return True
    except Exception:
        return False


def list_local_models() -> list:
    """Returns the chat-capable model names Ollama already has pulled on this machine."""
    try:
        req = urllib.request.Request(f"{OLLAMA_ROOT_URL}/api/tags", method="GET")
        with urllib.request.urlopen(req, timeout=5) as resp:
            data = json.loads(resp.read())
            names = [m["name"] for m in data.get("models", [])]
            return [n for n in names if "embed" not in n.lower()]
    except Exception:
        return []


def current_model() -> str:
    return st.session_state.get("selected_model", OLLAMA_MODEL)


def call_ollama(system: str, user: str, max_tokens: int = 500):
    """Returns (text, error). error is None on success."""
    model = current_model()
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "options": {"num_predict": max_tokens},
    }).encode()
    req = urllib.request.Request(
        OLLAMA_CHAT_URL, data=payload,
        headers={"Content-Type": "application/json"}, method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read())
            return result.get("message", {}).get("content", ""), None
    except urllib.error.HTTPError as e:
        # HTTPError is a subclass of URLError — Ollama IS running and reachable,
        # it just rejected this specific request (e.g. model not pulled yet).
        # Must be caught before the plain URLError branch below, or this message
        # never shows and the misleading "is Ollama running?" text does instead.
        body = e.read().decode(errors="replace")
        try:
            body = json.loads(body).get("error", body)
        except Exception:
            pass
        if "not found" in body.lower():
            return None, (
                f"Ollama is running, but '{model}' isn't available: {body} "
                f"Open Command Prompt and run: ollama pull {model}"
            )
        return None, f"Ollama returned an error (HTTP {e.code}): {body}"
    except urllib.error.URLError:
        return None, (
            "Can't reach Ollama. Is it running? Open Command Prompt and type: ollama serve "
            "(or check the Ollama icon in your system tray)."
        )
    except Exception as e:
        return None, f"Unexpected error: {e}"


def show_prompt(system: str, user: str):
    st.markdown("**📨 Exact prompt sent to the model:**")
    st.markdown(f"""
    <div class="prompt-box prompt-system">
        <div class="prompt-label sys-label">🟢 System — who the AI is</div>{system}
    </div>
    <div class="prompt-box prompt-user">
        <div class="prompt-label usr-label">🔵 User — the actual request</div>{user}
    </div>
    """, unsafe_allow_html=True)


def run_and_show(system: str, user: str, key: str, max_tokens: int = 500):
    if st.button("🚀 Run", key=key, type="primary"):
        t0 = time.perf_counter()
        with st.spinner(f"Asking {current_model()} (running locally on your laptop)…"):
            text, err = call_ollama(system, user, max_tokens=max_tokens)
        elapsed = time.perf_counter() - t0
        if err:
            st.error(f"❌ {err}")
        else:
            st.markdown("#### 📤 Output")
            st.markdown(text)
            st.caption(f"⏱ {elapsed:.1f}s · 100% local, zero API cost")
        return text, err
    return None, None


def notice(text: str):
    st.markdown(f'<div class="notice-box">💡 <b>What to notice:</b> {text}</div>', unsafe_allow_html=True)


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🧪 Prompt Playground")
    st.caption("Samsung GenAI Program · Day 2")
    st.divider()

    available_models = list_local_models()
    if available_models:
        default_idx = available_models.index(OLLAMA_MODEL) if OLLAMA_MODEL in available_models else 0
        chosen = st.selectbox("Model (auto-detected on your laptop):", available_models, index=default_idx)
        st.session_state.selected_model = chosen
        if OLLAMA_MODEL not in available_models:
            st.caption(f"💡 We recommend `{OLLAMA_MODEL}` for the fastest responses on a laptop CPU — run `ollama pull {OLLAMA_MODEL}` if you want to add it. Whatever's selected above will work too, just possibly slower.")
    else:
        st.session_state.selected_model = OLLAMA_MODEL
        st.warning(f"No local models detected yet. Defaulting to `{OLLAMA_MODEL}` — make sure you've run `ollama pull {OLLAMA_MODEL}`.")

    st.markdown(f'<span class="local-pill">🖥️ {current_model()} · 100% local</span>', unsafe_allow_html=True)
    st.caption("No API key. No internet needed after setup. Nothing leaves your laptop.")
    st.divider()
    if st.button("🔌 Test Ollama Connection"):
        if ollama_alive():
            st.success("✅ Ollama is running — you're good to go.")
        else:
            st.error("❌ Can't reach Ollama. Open Command Prompt → type: ollama serve")
    st.divider()
    st.caption("This is a bonus practice tool — not scored, not submitted. Come back to it anytime.")


# ── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="mission-banner">
    <h2>🧪 Prompt Playground</h2>
    <div class="tagline">Practice everything from today's session — instantly, for free, fully offline.</div>
</div>
""", unsafe_allow_html=True)

st.info(
    "This is your own local AI model — no ChatGPT/Claude/Gemini account needed here, "
    "no cost, and it works even without internet. First response after opening the app "
    "may take a few extra seconds while the model loads into memory — every response after that is faster."
)

tab1, tab2, tab3, tab4 = st.tabs([
    "1️⃣ Zero / One / Few-Shot",
    "🧩 6-Element Framework",
    "🧠 Chain-of-Thought",
    "🎨 Free Playground",
])


# ══════════════════════════════════════════════════════════════════════════
#  TAB 1 — SHOT-BASED PROMPTING
# ══════════════════════════════════════════════════════════════════════════
def build_shot_prompt(task: str, shot_type: str):
    if shot_type == "Zero-shot":
        system = "You are a Samsung customer support assistant."
        user = task
    elif shot_type == "One-shot":
        system = "You are a Samsung customer support assistant. Match the style of the example exactly."
        user = f"""EXAMPLE:
Customer issue: My Galaxy Watch battery drains too fast.
Reply: "Thanks for flagging this — fast battery drain is usually caused by an app running in the background. Try Settings > Battery > Background Usage Limits, and let us know if it continues so we can look deeper."

Now write a reply for: {task}"""
    else:  # Few-shot
        system = "You are a Samsung customer support assistant. Match our tone and format exactly across every reply."
        user = f"""EXAMPLE 1:
Customer issue: My Galaxy Watch battery drains too fast.
Reply: "Thanks for flagging this — fast battery drain is usually caused by an app running in the background. Try Settings > Battery > Background Usage Limits, and let us know if it continues so we can look deeper."

EXAMPLE 2:
Customer issue: My Galaxy Buds keep disconnecting.
Reply: "Sorry about the disconnects — please update to the latest Buds firmware via the Galaxy Wearable app, and re-pair from scratch. That resolves this in most cases."

Now write a reply for: {task}"""
    return system, user


with tab1:
    st.markdown("<div class='concept-box'>Zero-shot = no examples, just the ask. One-shot = one worked example first. Few-shot = 2+ examples. More examples usually means the AI matches your exact style more closely — at the cost of a longer prompt.</div>", unsafe_allow_html=True)

    task = st.text_area(
        "Customer issue to reply to:",
        value="My Galaxy S24 keeps overheating when I use the camera for more than 2 minutes.",
        height=70,
    )
    shot_type = st.radio("Strategy:", ["Zero-shot", "One-shot", "Few-shot"], horizontal=True)

    system, user = build_shot_prompt(task, shot_type)
    show_prompt(system, user)

    text, err = run_and_show(system, user, key="shot_run")
    if text:
        notice(f"You used <b>{shot_type}</b>. Now switch to a different strategy above and run again on the exact same issue — compare tone and structure.")


# ══════════════════════════════════════════════════════════════════════════
#  TAB 2 — 6-ELEMENT FRAMEWORK BUILDER
# ══════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("<div class='concept-box'>The 6 elements from Section 4 of today's content page: Role, Goal, Context, Constraints, Style/Tone, Output Format. Fill in as many as you like — the assembled prompt updates live below.</div>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)
    with c1:
        role = st.text_input("Role", placeholder="e.g. You are a Samsung Care+ senior support specialist")
        goal = st.text_input("Goal", placeholder="e.g. Draft a reply resolving the customer's issue")
        context = st.text_area("Context", placeholder="Background facts the AI has no way to know on its own", height=80)
    with c2:
        constraints = st.text_area("Constraints", placeholder="Length limit, must-include, must-avoid", height=80)
        style = st.text_input("Style / Tone", placeholder="e.g. Warm, professional, not scripted-sounding")
        output_fmt = st.text_input("Output Format", placeholder="e.g. Ready-to-send email, no placeholders")

    parts = []
    if role: parts.append(role)
    if goal: parts.append(goal)
    if context: parts.append(f"Context: {context}")
    if constraints: parts.append(f"Constraints: {constraints}")
    if style: parts.append(f"Tone: {style}")
    if output_fmt: parts.append(f"Output format: {output_fmt}")
    assembled = "\n\n".join(parts) if parts else "Fill in any field above — the assembled prompt appears here."

    st.markdown("**Assembled prompt:**")
    st.code(assembled, language="text")

    framework_system = "You are a helpful assistant."
    text, err = run_and_show(framework_system, assembled, key="framework_run")
    if text:
        notice("Now try removing one field (e.g. Output Format) and running again with everything else the same — that's exactly what a missing element costs in real usage.")


# ══════════════════════════════════════════════════════════════════════════
#  TAB 3 — CHAIN-OF-THOUGHT
# ══════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("<div class='concept-box'>Chain-of-Thought means instructing the model to reason step by step before giving a final answer, instead of jumping straight to it. Toggle it on and off on the exact same problem and compare.</div>", unsafe_allow_html=True)

    problem = st.text_area(
        "Your problem:",
        value="A Samsung store starts the day with 500 Galaxy Buds. It sells 15% of stock in the morning, then receives a restock of 80 units. In the afternoon it sells 40 more units. How many units are left by closing?",
        height=80,
    )
    use_cot = st.toggle("🧠 Enable step-by-step reasoning (Chain-of-Thought)", value=True)

    cot_system = "You are a helpful assistant."
    if use_cot:
        cot_user = f"{problem}\n\nWork through this step by step, showing each calculation, then give the final answer clearly."
    else:
        cot_user = problem

    show_prompt(cot_system, cot_user)
    text, err = run_and_show(cot_system, cot_user, key="cot_run", max_tokens=600)
    if text:
        if use_cot:
            notice("Now turn Chain-of-Thought OFF and run again on the same problem. Compare: did the naive version skip a step or make a silent arithmetic error?")
        else:
            notice("That was the raw, naive answer. Now turn Chain-of-Thought ON and run again — compare the reasoning and the final number.")


# ══════════════════════════════════════════════════════════════════════════
#  TAB 4 — FREE PLAYGROUND
# ══════════════════════════════════════════════════════════════════════════
with tab4:
    st.markdown("<div class='concept-box'>Open exploration — write any System and User prompt you like and see what comes back. Try combining techniques from the other tabs.</div>", unsafe_allow_html=True)

    free_system = st.text_area("System (Role):", value="You are a helpful assistant.", height=70)
    free_user = st.text_area("User (your question):", value="", height=100, placeholder="Type anything you want to try…")

    if free_user.strip():
        show_prompt(free_system, free_user)
        run_and_show(free_system, free_user, key="free_run", max_tokens=700)
    else:
        st.caption("Type something in the User box above to enable Run.")
