# Day 3 — Foundation Models and Platforms
**Samsung GenAI Program · SRM Kattankulathur · 15 July 2026**

No fork/clone setup today — you already did that on Day 1. Pull today's folder the same way you always do:

```bash
git pull upstream main
```

(Your trainer will confirm this on the projector before Part 2 — it also brings you a new local tool this time, see Part 2 Step 1 below.)

---

## Part 1 — Lecture & Content
Open today's content page from the URL on the projector: `day3/index.html`

Work through Sections 1–10 at the trainer's pace. Section 11 (Practice Quiz) is optional and not scored — use it whenever you want a confidence check.

---

## Part 2 — Lab 1: AI Interrogation Room
**AM · Individual · Scored · ~45 minutes (includes a 30-min live walkthrough first)**

### Step 1 — Get the app running
This is a small local tool, not a webpage — it needs to actually run on your laptop, same as Day 2's Prompt Playground.

- Already set up Ollama for the Prompt Playground? Skip straight to running it.
- First time? Follow `day3/interrogation_room/SETUP.md` — install Ollama → pull a model → confirm Python → install Streamlit.

Then, from inside your `samsung-genai` folder:
```bash
cd day3/interrogation_room
streamlit run app.py
```

### Step 2 — Watch the live walkthrough
Your trainer projects the app and runs one hallucination trap, one bias probe, and one guardrail block-then-bypass live, before you touch your own laptop. Watch first.

### Step 3 — Work through all 4 modules yourself
Open `day3/lab/lab1.html` for the full step-by-step checklist. In short:
1. **Hallucination Lab** — fire at least 1 pre-planted trap, then Fix It on the same one
2. **Bias Probe** — run at least 1 probe, compare Run A vs. Run B output
3. **Guardrail Builder** — write your own system prompt, test it against a dangerous request
4. **Guardrail Battle** — complete all 8 attacks. If your blocked score is below 5/8, go back and rewrite your guardrail, then **Reset Battle** and try again — iterating is expected, not a failure.

### Step 4 — Copy your results
Open **📤 My Results** in the app's sidebar (last item). It shows your checklist and Guardrail Battle score in a copy-paste-ready block. Keep this open, or copy the numbers into a notes app — you'll need them for Lab 2.

**Nothing submits from Lab 1 itself** — its numbers get folded into Lab 2's combined submission.

---

## Part 3 — Lab 2: RAG vs. No-RAG Showdown
**PM · Individual · Scored**

### Step 1 — Open Lab 2
Open the URL shown on the projector, or `day3/lab/lab2.html`.

### Step 2 — Pick one scenario
Click one of 3 scenario cards (A — Care+ Warranty, B — HR Parental Leave, C — Product Spec).

### Step 3 — Run 1: No-RAG
Paste only the question (no document) into any one AI tool, fresh chat. Summarize what it said — was it actually right, or just confident-sounding?

### Step 4 — Run 2: RAG
New chat, same tool. This time paste the instruction to use *only* the provided information, then the document from your scenario card, then the same question. Summarize the grounded answer.

### Step 5 — Judge the difference
Pick whichever actually happened: RAG fixed a wrong answer, RAG confirmed an already-right answer, or there was no real difference. All three are valid findings.

### Step 6 — Fill in the Interrogation Room Recap
Using your **📤 My Results** numbers from Lab 1, tick the 4 checkboxes and enter your Guardrail Battle blocked/total score.

**Stretch (optional):** either find a case where the RAG document conflicts with what the model already "knew," or go back to the Interrogation Room and design your own attack in Free Input / Guardrail Battle.

---

## Part 4 — Submit day3.json (covers Lab 1 + Lab 2, one file)

Same download-generator flow as Day 2 — no Notepad editing needed.

### Step 1 — Scroll to "Submit" at the bottom of Lab 2
Fill in every field: your name, GitHub username, your RAG scenario/summaries/judgement, and your Interrogation Room Recap checkboxes + battle score.

Watch the JSON preview box update live, and the task counter show how many of the 6 core tasks are detected as complete.

### Step 2 — Click "Generate & Download day3.json"
Your browser saves a file named exactly `day3.json` into your **Downloads** folder — already valid JSON, already correctly named.

> If the download button doesn't work for any reason, click **Copy JSON instead**, then paste into Notepad and save manually as `day3.json` inside `submissions/` (Save as type: **All Files**).

### Step 3 — Move the file into your submissions folder
Open File Explorer → go to your **Downloads** folder → find `day3.json` → move it into your `samsung-genai/submissions/` folder.

### Step 4 — Push via Git Bash
1. Open File Explorer → go to your `samsung-genai` folder (not submissions)
2. Right-click on empty space → **Git Bash Here**
3. Run these 3 commands one by one:

```bash
git add submissions/day3.json
git commit -m "Day 3 submission - YOUR NAME"
git push origin main
```

Replace `YOUR NAME` with your actual name in the commit message.

### Step 5 — Check your badge on the dashboard
Open the dashboard URL from the projector. Within a minute you'll see your badge for Day 3:

| Badge | What it means |
|---|---|
| 💎 Diamond | 100% of the 6 core tasks done AND Guardrail Battle ≥7/8 blocked AND stretch task done |
| 🥇 Gold | At least 80% of the 6 core tasks done AND Guardrail Battle ≥5/8 blocked |
| 🥈 Silver | Submitted with your name filled in |

> Today is different from Day 1/2 — Gold and Diamond both require a minimum Guardrail Battle score, not just task completion. That score is computed automatically from what the model actually did in your battle, not self-reported, so it's worth iterating on your guardrail if your first run falls short.

---

## From Day 4 onwards
Each day follows this same pattern: open that day's lab(s) from the projector URL, complete them, use the built-in generator at the end to download that day's submission file, move it into `submissions/`, then push with the day's file name.
