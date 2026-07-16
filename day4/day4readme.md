# Day 4 — AI Ethics and Responsibility
**Samsung GenAI Program · SRM Kattankulathur · 16 July 2026**

No fork/clone setup today — you already did that on Day 1. Pull today's folder the same way you always do:

```bash
git pull upstream main
```

(Your trainer will confirm this on the projector before Part 2.)

---

## Part 1 — Lecture & Content
Open today's content page from the URL on the projector: `day4/index.html`

Work through Sections 1–11 at the trainer's pace. Section 12 (Practice Quiz) is optional and not scored — use it whenever you want a confidence check.

---

## Part 2 — Lab 1: Incident Investigator
**Individual · Scored**

### Step 1 — Open the lab
Open the URL shown on the projector, or `day4/lab/lab1.html`.

### Step 2 — Read all 6 incident files
Each card (A–F) is a real AI failure with the company name stripped out. Click a card to expand it and read the summary.

### Step 3 — Classify each incident
For each of the 6 files, pick:
- **Failure type** — Hallucination, Bias/Discrimination, Privacy Violation, Deepfake/Misinformation, Lack of Human Oversight, or Security Breach
- **Principle violated hardest** — one of the 10 Responsible AI principles from Section 4 of today's content page

There's no answer key shown in the app — this is your own judgement call, the same one a real governance analyst has to make.

### Step 4 — Write your justifications
Write a one-line justification for at least 4 of the 6 files (all 6 if you have time) — why that failure type, why that principle.

**Stretch (optional):** research and write up one additional real AI-failure case not covered in today's content — use the real company name this time.

---

## Part 3 — Submit day4.json

Same download-generator flow as Days 2–3 — no Notepad editing needed.

### Step 1 — Scroll to "Submit" at the bottom of Lab 1
Fill in your name and GitHub username. Watch the JSON preview box update live, and the counter show how many of the 6 incidents are fully classified.

### Step 2 — Click "Generate & Download day4.json"
Your browser saves a file named exactly `day4.json` into your **Downloads** folder — already valid JSON, already correctly named.

> If the download button doesn't work for any reason, click **Copy JSON instead**, then paste into Notepad and save manually as `day4.json` inside `submissions/` (Save as type: **All Files**).

### Step 3 — Move the file into your submissions folder
Open File Explorer → go to your **Downloads** folder → find `day4.json` → move it into your `samsung-genai/submissions/` folder.

### Step 4 — Push via Git Bash
1. Open File Explorer → go to your `samsung-genai` folder (not submissions)
2. Right-click on empty space → **Git Bash Here**
3. Run these 3 commands one by one:

```bash
git add submissions/day4.json
git commit -m "Day 4 submission - YOUR NAME"
git push origin main
```

Replace `YOUR NAME` with your actual name in the commit message.

### Step 5 — Check your badge on the dashboard
Open the dashboard URL from the projector. Within a minute you'll see your badge for Day 4:

| Badge | What it means |
|---|---|
| 💎 Diamond | All 6 incidents fully classified AND the stretch case completed |
| 🥇 Gold | At least 80% (5 of 6) incidents fully classified |
| 🥈 Silver | Submitted with your name filled in |

---

## From Day 5 onwards
Day 5 is your Chapter 5 mini-project day — pick one of the 4 project topics in `project/GenAI_Capstone_Project_Brief.md` (already in your repo) ahead of time if you'd like to start thinking about it.
