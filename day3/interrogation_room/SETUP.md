# AI Interrogation Room — Setup & Run Guide
**Samsung GenAI Program · Day 3 · Lab 1 — scored, submitted via Lab 2**

This is a small app that runs entirely on your own laptop. It uses a real local AI model (no ChatGPT/Claude/Gemini account, no API key, no internet needed once set up) so you can put an AI under pressure yourself — trigger hallucinations, catch bias, then build and attack your own safety guardrail. Everything runs for free, as many times as you like.

> **Already set up Ollama for the Day 2 Prompt Playground?** Skip straight to **Step 5**.

There are steps: install Ollama → download a model → check Python → install Streamlit → get the app → run it. Follow them in order.

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
3. You should see a version number. If you see "not recognized," the install didn't complete — reopen the installer from Step 1.

---

## Step 2 — Download a model

This app works with **any** chat model you already have pulled — it auto-detects whatever's installed and lets you pick from a dropdown. If you don't have one yet:

1. In Command Prompt, type:
   ```
   ollama pull llama3.2:1b
   ```
2. Press Enter and wait — this downloads the model (a few minutes depending on WiFi). You'll see a progress bar.
3. Verify it downloaded:
   ```
   ollama list
   ```

Already have `qwen2.5:7b` or another chat model pulled from earlier work? That's fine too — the app will list it and you can select it instead. Bigger models answer slower on a laptop CPU but work the same way.

---

## Step 3 — Check Python is installed

1. In Command Prompt, type:
   ```
   python --version
   ```
2. **If you see a version number** — skip to Step 4.
3. **If you see "not recognized"** — Python isn't installed:
   - Go to `https://www.python.org/downloads/`
   - Click the yellow **Download Python** button and run the installer
   - **Critical: on the very first installer screen, tick "Add python.exe to PATH" before clicking Install.**
   - Close and reopen Command Prompt, then re-run `python --version` to confirm.

---

## Step 4 — Install Streamlit

In Command Prompt:
```
pip install streamlit
```
If you see `pip: not recognized`, Python's PATH setup didn't complete — go back to Step 3 and reinstall with the PATH checkbox ticked.

---

## Step 5 — Get the app files

1. Open File Explorer → go to your `samsung-genai` folder
2. Right-click on empty space → **Git Bash Here**
3. Type:
   ```bash
   git pull origin main
   ```
4. This pulls the `interrogation_room/` folder into your existing clone.

---

## Step 6 — Run the app

1. In Command Prompt, navigate into the app folder (replace the path with wherever you cloned `samsung-genai`):
   ```
   cd samsung-genai\interrogation_room
   ```
2. Type:
   ```
   streamlit run app.py
   ```
3. Your browser should open automatically to `http://localhost:8501`. If it doesn't, open that address manually in Chrome or Edge.
4. In the sidebar, click **🔌 Test Ollama Connection** — it should say "✅ Ollama is running." If not, see Troubleshooting below.
5. Start with **🏠 Briefing**, then work through the 4 modules in order.

> To stop the app: go back to the Command Prompt window and press **Ctrl+C**.
> Running this alongside the Prompt Playground? Each `streamlit run` uses its own port automatically (8501, 8502, ...) — you can have both open at once.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `'python'` / `'pip'` / `'streamlit'` not recognized | Python isn't on PATH — reinstall from python.org with "Add python.exe to PATH" ticked. |
| App says "Can't reach Ollama" | Ollama isn't running. Check the llama icon in your system tray, or open Command Prompt and type `ollama serve`. |
| "No local models detected" in the sidebar | You haven't pulled a model yet — run `ollama pull llama3.2:1b` (Step 2). |
| First response is slow | Normal — the model loads into memory on first use. Every response after is faster. |
| `Address already in use` | Another Streamlit app (maybe the Prompt Playground) is already running. Either close it, or run `streamlit run app.py --server.port 8502`. |

---

## What each module does

| Module | What you're practicing |
|---|---|
| 1️⃣ Hallucination Lab | Fire pre-planted traps designed to make the model invent a confident, wrong answer — then fix it by adding grounding context |
| 2️⃣ Bias Probe | Run a biased vs. corrected prompt side by side and see exactly what changes |
| 3️⃣ Guardrail Builder | Write a system prompt yourself and test whether it stops a dangerous request |
| 4️⃣ Guardrail Battle | 8 increasingly sophisticated attacks try to break your guardrail — predict before each one fires |

This tool isn't scored and there's nothing to submit — come back to it whenever you want to explore how hallucinations, bias, and guardrails actually work under the hood.
