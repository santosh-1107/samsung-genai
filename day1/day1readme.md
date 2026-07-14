# Day 1 — Introduction to GenAI
**Samsung GenAI Program · SRM Kattankulathur · 13 July 2026**

## Start here — do these 3 steps in order, before anything else

**1. Go to the trainer's GitHub repo:**
`https://github.com/Anilmidna/samsung-genai`

**2. Click the Fork button** (top-right of that page) → **Create fork**.
Wait until the browser address bar shows `github.com/YOUR-USERNAME/samsung-genai` — that's your own personal copy. You now own it; the trainer's copy is untouched.

**3. You're now working from your fork, not the trainer's repo.** Every step below — cloning, labs, submissions — happens inside *your* copy. If you ever need to come back to these instructions, they also live inside your fork at `day1/day1readme.md`.

---

## Part 1 — One-Time Setup (Day 1 Only)

> You do this only today. From Day 2 onwards, skip to Part 2.

### 1A — Verify your AI accounts
Open each of these in a browser tab and confirm you can log in:

| Tool | URL | Model to use |
|---|---|---|
| ChatGPT | chat.openai.com | GPT-4o |
| Claude | claude.ai | Claude Sonnet |
| Gemini | gemini.google.com | Gemini 1.5 Pro |

---

### 1B — Clone your fork to your laptop
1. Press **Windows key** → type **Git Bash** → press Enter
2. A black terminal window opens. Type these commands one line at a time:

```bash
git clone https://github.com/YOUR-USERNAME/samsung-genai.git
cd samsung-genai
```

Replace `YOUR-USERNAME` with your actual GitHub username (the fork you created in Step 2 above — not the trainer's).

3. You should see a `samsung-genai` folder appear on your Desktop or Documents.

---

## Part 2 — Lab 1: Tool Setup & Pipeline Test
**Not scored · ~30 minutes**

This lab proves your entire submission pipeline works before any scored lab begins.

---

### Step 1 — Open checkin.json
1. Press **Windows key + E** to open File Explorer
2. Navigate to where you cloned the repo (Desktop or Documents)
3. Open `samsung-genai` folder → open `submissions` folder
4. Right-click **checkin.json** → **Open with** → **Notepad**

You will see:
```json
{
  "student_name": "Type Your Full Name Here",
  "github": "your-github-username",
  "team": "TBD",
  "status": "ready"
}
```

---

### Step 2 — Edit two fields only
Change **only** these two lines. Do not touch anything else:
- `"student_name"` → replace with your full name (e.g. `"Rahul Kumar"`)
- `"github"` → replace with your GitHub username (e.g. `"rahulkumar2024"`)

Press **Ctrl+S** to save. Close Notepad.

---

### Step 3 — Push to GitHub
1. In File Explorer, go back up to the `samsung-genai` folder (not submissions)
2. Right-click on empty space inside the folder → click **Git Bash Here**
3. A black terminal opens. Type these 3 commands one by one:

```bash
git add submissions/checkin.json
git commit -m "Day 1 check-in"
git push origin main
```

4. If asked for a username and password, enter your GitHub credentials.

---

### Step 4 — Confirm on dashboard
Look at the projector. Within 30 seconds your name should appear as a **green tick**.

If it does — your pipeline works. You are ready for the scored labs.

---

## Part 3 — Lab 2: Next Word Prediction
**Team activity · ~45 minutes + 20 min Gradio Showdown**

---

### Step 1 — Find your team
Trainer will announce 10 teams of 4 students. Find your teammates.
One person in each team is the **Team Lead** — they will present the Gradio demo.

---

### Step 2 — Open the notebook
Open Lab 2 from the URL on the projector. Click **Open in Google Colab**.
In Colab: **File → Save a copy in Drive** (so you can edit it).

---

### Step 3 — Complete all 8 Missions
Run each cell in order. Key missions:

| Mission | What to do |
|---|---|
| 1 | Install libraries — run cell, no errors |
| 2 | Imports — run cell |
| 3 | Choose ONE model — uncomment only one line |
| 4 | Load model — wait for "Model Loaded" |
| 5 | Tokenization — note vocab size and token count |
| 6 | Fill in the 3 TODOs (logits, softmax, top-k) |
| 7 | Test with different prompts |
| 8 | Run `demo.launch(share=True)` → copy the `gradio.live` URL |

---

### Step 4 — Note your Gradio URL
After Mission 8 runs, you will see a line like:
```
Running on public URL: https://abc123def456.gradio.live
```
**Copy this URL and keep it** — you need it when filling day1.json after Lab 3.

---

### Step 5 — Present your demo (Gradio Showdown)
Trainer calls each team. Team Lead connects to projector and opens the Gradio URL.
You have **2 minutes** to show:
- Which model you used and why
- Your most interesting prediction
- What you learned about how transformers work

---

## Part 4 — Lab 3: AI Trust Audit
**Individual · Scored · ~60–75 minutes**

You are a Junior AI Quality Analyst today — not rating "which chatbot sounds nicer," but independently verifying whether ChatGPT, Claude, and Gemini can be trusted with real tasks. Three investigations, each testing a different failure mode, then a synthesis.

---

### Step 1 — Open Lab 3
Open the URL shown on the projector.

---

### Step 2 — Set up your models
Before every prompt (including both runs of Investigation 3), open a **new chat**:
- ChatGPT: Settings → Personalization → Memory → turn **OFF**
- Claude: open a new conversation
- Gemini: open a new conversation

---

### Step 3 — Investigation 1: Technical Fact Hallucination
1. Copy the Investigation 1 prompt exactly, run it in all 3 models
2. Independently verify every specific claim (chip names, on-device/cloud split) using a real Google search
3. Tick which model(s) stated something incorrect, classify it, and write your evidence on the lab page

---

### Step 4 — Investigation 2: Fabricated Citation Hallucination
1. Copy the Investigation 2 prompt exactly, run it in all 3 models
2. Try to actually find the paper/report each model names — search Google Scholar and research.samsung.com
3. Tick which model(s) named something you couldn't verify, classify it, and write your evidence (the exact title/authors/year given, and what your search found)

---

### Step 5 — Investigation 3: Bias Swap Test
1. Pick **one** model for this investigation
2. Copy **Run A** exactly (candidate name: Arjun Mehta), run it in a fresh chat, save the score + reasoning
3. Copy **Run B** exactly (candidate name: Ananya Mehta — identical qualifications, only the name changed), run it in a **new** fresh chat, save the score + reasoning
4. Compare the two side by side — same facts, did the score or the tone of the reasoning differ? Mark Yes/No and write your evidence

---

### Step 6 — Write your AI Trust Report
At the bottom of Lab 3, write 3–5 sentences synthesizing all 3 investigations: what pattern did you notice, and would you trust these tools unsupervised for a customer-facing or hiring-related task? **This is required for Gold.**

---

### Step 7 — Fill in your Lab 2 Recap
Near the bottom of Lab 3, paste your team name, the model you used, and your Gradio URL from Lab 2 — then tick the confirmation box that the link was live during the Showdown. **This is what makes your Lab 2 work count toward your Diamond badge** — Lab 2 itself isn't graded separately.

---

### Step 8 (Stretch) — Design your own investigation
Finished early? Design a 4th investigation testing privacy, copyright, or safety — any Responsible AI dimension not already covered above. Run it, document it. **This feeds your Diamond badge.**

---

## Part 5 — Submit day1.json (After Lab 3)

This covers BOTH Lab 2 and Lab 3 in one file. One push at the end of the day.

---

### Step 1 — Fill in your name and GitHub username
Near the bottom of Lab 3, under "Your Details," enter your full name and GitHub username. Everything else you typed earlier on the page (both investigations, the bias swap test, your synthesis, Lab 2 recap, stretch) is assembled automatically — you don't need to retype anything.

---

### Step 2 — Generate and download your submission
Scroll to "Generate your submission file." Check the task counter — it should say **5 / 5 core tasks detected as complete** if you finished everything. Click **⬇ Generate & Download day1.json**.

Your browser saves the file already correctly named and typed into your **Downloads** folder — no Notepad editing needed.

> If the download button doesn't work for any reason, click **Copy JSON instead**, then open Notepad, paste, and save manually as `day1.json` inside `submissions/` — **Save as type: All Files (*.*)**, not "Text Documents" (otherwise it saves as `day1.json.txt` and the dashboard cannot read it).

Field reference, in case you want to double-check what each part means:

| Field | What it captures |
|---|---|
| `student_name` / `github` | Your name and GitHub username |
| `lab2_team` / `lab2_model_used` / `lab2_gradio_url` | Your Lab 2 recap |
| `h1_classification` / `h1_evidence` | Investigation 1 (technical fact hallucination) |
| `h2_classification` / `h2_evidence` | Investigation 2 (fabricated citation hallucination) |
| `b1_run_a` / `b1_run_b` / `b1_bias_detected` / `b1_evidence` | Investigation 3 (bias swap test) |
| `synthesis` | Your AI Trust Report |
| `stretch_done` / `stretch_scenario` / `stretch_evidence` | Your stretch investigation, if you did one |
| `tasks_completed` / `tasks_total` | Auto-counted out of 5: Investigation 1, 2, 3, Synthesis, verified Lab 2 link |

---

### Step 3 — Move day1.json into the submissions folder
1. Open File Explorer → go to your **Downloads** folder → find `day1.json`
2. Drag-and-drop (or cut-paste) it into `samsung-genai/submissions/`
3. Don't rename it — it must stay exactly `day1.json`

---

### Step 4 — Push to GitHub

1. Open File Explorer → go to your `samsung-genai` folder (not submissions)
2. Right-click on empty space → **Git Bash Here**
3. Type these 3 commands one by one:

```bash
git add submissions/day1.json
git commit -m "Day 1 submission - YOUR NAME"
git push origin main
```

Replace `YOUR NAME` with your actual name in the commit message.

---

### Step 5 — Check your badge on the dashboard
Open the dashboard URL from the projector. Within 30 seconds you will see your badge:

| Badge | What it means |
|---|---|
| 💎 Diamond | Gold + a verified Lab 2 Gradio link + the stretch investigation completed |
| 🥇 Gold | 4 of 5 core tasks done (Investigations 1–3 + Synthesis) |
| 🥈 Silver | Submitted with your name filled in |

> The badge is calculated automatically from what you put in day1.json. You cannot choose it yourself.

---

## How Days 2–5 Work

From Day 2 onwards you already have your fork and clone. No setup needed.

Each day:
1. Open that day's lab(s) from the URL on the projector
2. Complete all labs
3. Fill in the submission form built into the last lab, then click **Generate & Download** — your browser saves the file already correctly named and typed, no Notepad editing needed (see that day's own readme for exact steps)
4. Move the downloaded file into `submissions/`, then push:

```bash
git add submissions/day2.json
git commit -m "Day 2 submission - YOUR NAME"
git push origin main
```

Change the day number each day. Everything else is identical.
