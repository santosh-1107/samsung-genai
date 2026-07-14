# Day 2 — Prompt Engineering Basics
**Samsung GenAI Program · SRM Kattankulathur · 14 July 2026**

No setup today — you already forked and cloned the repo on Day 1. If you're on a new machine, see Day 1's `day1readme.md` first.

---

## Part 1 — Lecture & Content
Open today's content page from the URL on the projector: `day2/index.html`

Work through Sections 1–9 at the trainer's pace. Section 10 (Practice Quiz) is optional and not scored — use it whenever you want a confidence check.

---

## Part 2 — Lab 1: Prompt Framework Builder
**AM · Individual or pairs · Not directly submitted — feeds into Lab 2**

### Step 1 — Open Lab 1
Open the URL shown on the projector, or `day2/lab/lab1.html` inside your cloned repo.

### Step 2 — Pick one scenario
Click one of the 3 scenario cards (A, B, or C).

### Step 3 — Write your 6-element prompt
Fill in Role, Goal, Context, Constraints, Style/Tone, and Output Format. Watch the assembled prompt build live underneath as you type.

### Step 4 — Run it and check it
Copy your assembled prompt into ChatGPT, Claude, or Gemini. Read the response, then check it against your own Constraints — did it actually follow every one?

**Remember (don't lose this):**
- Which scenario you picked (A / B / C)
- Your full assembled prompt
- Whether the output met your constraints

You'll type these into Lab 2's submission generator at the end of the day — nothing to save from Lab 1 itself.

**Stretch (optional):** repeat Steps 2–4 for one or two more scenarios, or add a strict output format (e.g. force valid JSON) to your first prompt and re-run it.

---

## Part 3 — Lab 2: Reasoning Upgrade
**PM · Individual · Scored**

### Step 1 — Open Lab 2
Open the URL shown on the projector, or `day2/lab/lab2.html`.

### Step 2 — Run the Naive Prompt
The page gives you one fixed prompt — copy it exactly, don't edit it. Paste it into any one AI tool. Summarize what it answered and whether it showed its reasoning.

### Step 3 — Write and run your own Chain-of-Thought Prompt
Using Section 6's pattern from today's content page, rewrite the same problem so the model must reason step by step before giving a final number. Run it, then summarize the step-by-step answer.

### Step 4 — Compare
Pick which approach you'd actually trust for a real decision — Naive or Chain-of-Thought — and why.

**Stretch (optional):** write a ReAct-style prompt that asks the model to call out where it would need a real tool or calculation instead of guessing.

---

## Part 4 — Submit day2.json (covers Lab 1 + Lab 2, one file)

This is different from Day 1 — you don't copy-paste into Notepad. Lab 2's page builds the file for you.

### Step 1 — Scroll to "Submit" at the bottom of Lab 2
Fill in every field:
- Your full name and GitHub username
- Your Lab 1 scenario, your assembled prompt, and whether it met your constraints
- Your Lab 2 naive/Chain-of-Thought summaries and which one you trust more

Watch the JSON preview box update live as you type, and the task counter show how many of the 6 core tasks are detected as complete.

### Step 2 — Click "Generate & Download day2.json"
Your browser saves a file named exactly `day2.json` into your **Downloads** folder — already valid JSON, already correctly named. No Notepad, no "Save as type" step, no risk of an accidental `.txt` extension.

> If the download button doesn't work for any reason, click **Copy JSON instead**, then paste into Notepad and save manually as `day2.json` inside `submissions/` (Save as type: **All Files**) — same fallback process as Day 1.

### Step 3 — Move the file into your submissions folder
Open File Explorer → go to your **Downloads** folder → find `day2.json` → move it into your `samsung-genai/submissions/` folder (drag-and-drop, or cut-paste).

### Step 4 — Push via Git Bash
1. Open File Explorer → go to your `samsung-genai` folder (not submissions)
2. Right-click on empty space → **Git Bash Here**
3. Run these 3 commands one by one:

```bash
git add submissions/day2.json
git commit -m "Day 2 submission - YOUR NAME"
git push origin main
```

Replace `YOUR NAME` with your actual name in the commit message.

### Step 5 — Check your badge on the dashboard
Open the dashboard URL from the projector. Within a minute you'll see your badge for Day 2:

| Badge | What it means |
|---|---|
| 💎 Diamond | All 6 core tasks done AND you completed the stretch (ReAct prompt) |
| 🥇 Gold | At least 80% of the 6 core tasks done |
| 🥈 Silver | Submitted with your name filled in |

> The badge is calculated automatically from what's in day2.json. You cannot choose it yourself.

---

## Bonus — Prompt Playground (not scored, not submitted)

A small local AI practice tool lives at `day2/prompt_playground/`. It runs a real AI model (Ollama, `llama3.2:1b`) 100% on your own laptop — no ChatGPT/Claude/Gemini account, no API key, no cost, works offline. Use it to practice zero/one/few-shot, the 6-element framework, and Chain-of-Thought with instant feedback, as many times as you like.

Full setup steps (Ollama install → model download → Python check → running the app) are in `day2/prompt_playground/SETUP.md`. **Start the model download early** — do it in the background while you're working through Lab 1 or Lab 2, since it takes a few minutes over classroom WiFi.

This is a bonus tool, not a lab — nothing to submit, no badge tie-in. Come back to it anytime.

---

## From Day 3 onwards
Each day follows this same pattern: open that day's lab(s) from the projector URL, complete them, use the built-in generator at the end to download that day's submission file, move it into `submissions/`, then push with the day's file name (e.g. `day3.json`).
