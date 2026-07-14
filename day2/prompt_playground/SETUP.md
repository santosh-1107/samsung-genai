# Prompt Playground — Setup & Run Guide
**Samsung GenAI Program · Day 2 · Bonus practice tool — not scored, not submitted**

This is a small app that runs entirely on your own laptop. It uses a real local AI model (no ChatGPT/Claude/Gemini account, no API key, no internet needed once set up) so you can practice everything from today's session — zero/one/few-shot, the 6-element framework, Chain-of-Thought — and get instant answers, for free, as many times as you like.

There are 4 steps: install Ollama → download a small model → check Python → run the app. Follow them in order.

---

## Step 1 — Install Ollama

Ollama is the free program that runs AI models locally on your laptop.

1. Open a browser and go to: `https://ollama.com/download/windows`
2. Click **Download for Windows**
3. Open the downloaded file (`OllamaSetup.exe`) and click through the installer — default options are fine
4. Once installed, Ollama runs quietly in the background. Look for its icon (a small llama) in your system tray (bottom-right of the taskbar, click the ^ arrow to see hidden icons if you don't see it)

### Verify it installed correctly
1. Press **Windows key**, type **cmd**, press Enter to open Command Prompt
2. Type this and press Enter:
   ```
   ollama --version
   ```
3. You should see a version number (e.g. `ollama version 0.x.x`). If you see "not recognized," the install didn't complete — reopen the installer from Step 1.

---

## Step 2 — Download the model

We're using **llama3.2:1b** — a small model (~1.3GB) chosen specifically so it runs fast on a laptop CPU with no GPU. Bigger models exist but are noticeably slower for this kind of live classroom exercise.

1. In the same Command Prompt window, type:
   ```
   ollama pull llama3.2:1b
   ```
2. Press Enter and wait — this downloads the model (a few minutes depending on WiFi speed). You'll see a progress bar.
3. When it finishes, verify it downloaded correctly:
   ```
   ollama list
   ```
   You should see `llama3.2:1b` in the list.

> ⚠️ **Do this on classroom WiFi as early as possible** — if everyone starts the download at the same time, it may take longer than expected. Start this now if you haven't already, even before finishing the rest of this guide.

### Quick test (optional but recommended)
Type:
```
ollama run llama3.2:1b
```
Type a message like `hello, are you working?` and press Enter. You should get a reply directly in the terminal. Type `/bye` to exit this test chat.

---

## Step 3 — Check Python is installed

1. In Command Prompt, type:
   ```
   python --version
   ```
2. **If you see a version number** (e.g. `Python 3.11.x`) — skip to Step 4.
3. **If you see "not recognized" or nothing** — Python isn't installed. Install it:
   - Go to `https://www.python.org/downloads/`
   - Click the yellow **Download Python** button
   - Run the installer
   - **Critical: on the very first installer screen, tick the checkbox "Add python.exe to PATH" at the bottom before clicking Install.** If you miss this, Python won't be usable from Command Prompt and you'll need to reinstall.
   - After installing, **close and reopen Command Prompt**, then re-run `python --version` to confirm.

---

## Step 4 — Install Streamlit

In Command Prompt, type:
```
pip install streamlit
```
Wait for it to finish (installs a handful of packages). If you see `pip: not recognized`, Python's PATH setup didn't complete correctly — go back to Step 3 and reinstall Python with the PATH checkbox ticked.

---

## Step 5 — Get the app files

If you already have the `samsung-genai` repo cloned from Day 1:
1. Open File Explorer → go to your `samsung-genai` folder
2. Right-click on empty space → **Git Bash Here**
3. Type:
   ```bash
   git pull origin main
   ```
4. This pulls the new `day2/prompt_playground/` folder into your existing clone.

If you don't have it cloned yet, see `day1readme.md`'s "Start here" section first, then come back to this step.

---

## Step 6 — Run the app

1. In Command Prompt, navigate into the app folder. Replace the path below with wherever you cloned `samsung-genai`:
   ```
   cd samsung-genai\day2\prompt_playground
   ```
2. Type:
   ```
   streamlit run app.py
   ```
3. Your browser should open automatically to `http://localhost:8501` showing the Prompt Playground. If it doesn't open automatically, open that address manually in Chrome or Edge.
4. In the app's sidebar, click **🔌 Test Ollama Connection** — it should say "✅ Ollama is running." If it says it can't connect, see Troubleshooting below.
5. Try each of the 4 tabs — type your own examples, not just the pre-filled ones.

> To stop the app later: go back to the Command Prompt window and press **Ctrl+C**.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `'python' is not recognized` | Python isn't on PATH. Reinstall Python from python.org and tick "Add python.exe to PATH" on the first installer screen. |
| `'pip' is not recognized` | Same root cause as above — fix Python's PATH first. |
| `'streamlit' is not recognized` | Try `python -m streamlit run app.py` instead of `streamlit run app.py`. |
| App says "Can't reach Ollama" | Ollama isn't running. Look for the llama icon in your system tray — if it's not there, open the Ollama app from the Start menu. Or open Command Prompt and type `ollama serve`. |
| First response takes a long time | Normal — the model has to load into memory the first time. Every response after that is faster. |
| `Address already in use` when running streamlit | Another app (or a previous run) is already using port 8501. Close the old Command Prompt window running streamlit, or run `streamlit run app.py --server.port 8502` and open `localhost:8502` instead. |
| Response quality feels basic | Expected — `llama3.2:1b` is a small model chosen for speed on laptop CPUs, not for perfect answers. The point is comparing prompting *techniques*, not getting production-quality output. |
| Model download is very slow | Everyone downloading at once saturates classroom WiFi. If it's taking too long, ask a neighbour who's already finished to share via a USB drive, or wait it out — it only needs to happen once. |

---

## What each tab does

| Tab | What you're practicing |
|---|---|
| 1️⃣ Zero / One / Few-Shot | Same customer-reply task, 3 ways — watch how adding examples changes the output |
| 🧩 6-Element Framework | Build a prompt from Role/Goal/Context/Constraints/Style/Output — same framework as Lab 1 |
| 🧠 Chain-of-Thought | Toggle step-by-step reasoning on/off on the same problem and compare |
| 🎨 Free Playground | Write any System + User prompt you like — open exploration |

This tool isn't scored and there's nothing to submit — come back to it whenever you want to test an idea before writing it into a lab.
