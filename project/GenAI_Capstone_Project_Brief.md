# GenAI Module — Final Mini Project Brief

## Where This Fits

You've completed 4 days of lecture and hands-on practice covering:

| Chapter | Topic |
|---|---|
| 1 | Evolution & Fundamentals of Generative AI (LLMs, Code/Image/Video models, vibe coding) |
| 2 | Prompt Engineering Basics (6-element structuring, zero-shot/few-shot, advanced prompting) |
| 3 | Foundation Models and Platforms (model internals, applying foundation models, platform comparison) |
| 4 | AI Ethics and Responsibility (bias, hallucination, guardrails, Responsible AI) |

Now you'll apply all of it in one **Final Mini Hands-on Project** — a real Samsung product/service scenario solved end-to-end using GenAI. **You choose ONE of the four project topics below** — read all four summaries first, then pick the one that interests you most. All four are equally valid choices; none is "easier" than another.

**Project Workflow (all topics follow this arc):**
1. Introduction and project definition
2. Data engineering and analysis
3. AI solution design
4. Prototype implementation (output development)
5. Short presentation + instructor feedback

**Tools:**
- Google Gemini (primary tool for all four projects; PJ3 specifically needs **Gemini Canvas**)
- Jupyter Notebook (PJ1, PJ2, PJ3)
- Anaconda (environment setup for PJ1, PJ2, PJ3)
- Optional: ChatGPT/Claude (text), Stable Diffusion (image) — if Gemini isn't available in your region, use another free GenAI tool, but note PJ3's Canvas step may not carry over.

**Evaluation:** Mini Project (80%) + Presentation (20%). No separate certificate for the GenAI module — it's a required, ungraded-standalone component of your overall course (90% attendance required).

**How to read each section below:** every step tells you *exactly* what to produce and gives you a **ready-to-paste example prompt** where GenAI is involved. You are not being asked to write code from scratch or invent a dataset out of thin air — Samsung hasn't handed you a real database for this exercise, so part of the exercise is *using GenAI itself to generate a realistic mock dataset*, then working with that.

---

## PJ1 — Mobile Product Recommendation System

**Samsung context:** Samsung Mobile + Recommendation Logic Development

**Scenario:** Samsung Mobile's e-commerce team wants a tool that suggests the right Galaxy phone to a shopper based on their needs — a mini shopping assistant. You're building a working prototype.

**Outcome:** An interactive UI where a user picks or describes a persona and gets a ranked phone recommendation with a reason.

### Step-by-step

**1. Set up Anaconda + Jupyter**
Confirm `jupyter notebook` launches from Anaconda Navigator or terminal. If you're stuck, this is identical to the setup you did on Day 1 for the Colab/local environment.

**2. Understand personas and recommendation systems**
A **persona** is a fictional but realistic customer profile representing a segment of real buyers — not a single individual, a *type*. Example:
> *"Priya, 24, photography enthusiast. Budget ₹40,000–60,000. Cares most about camera quality and screen size; doesn't care about gaming performance."*

You'll define 3–4 personas like this before you touch any scoring logic.

**3. Generate your mock dataset (since no real Samsung data is provided)**
Paste this into Gemini/ChatGPT:
> *"Generate a table of 15 Samsung Galaxy phone models (mix of budget, mid-range, and flagship) with these columns: model_name, price_inr, ram_gb, storage_gb, camera_mp, battery_mah, screen_size_inch, target_segment (one of: gaming, photography, business, budget). Base it on realistic 2024–2025 Galaxy lineup specs. Output as a markdown table."*

Copy the result into a spreadsheet or directly into your notebook as a Python list of dicts.

**4. Clean the data**
GenAI-generated data sometimes has duplicates, unrealistic prices, or inconsistent units. Scan for:
- Two rows with near-identical specs but different names (likely a duplicate — merge or remove)
- A budget phone priced above ₹80,000, or a flagship under ₹15,000 (unrealistic — fix manually)
- Missing values in any column

**5. Explore the data (EDA)**
Paste your table back into GenAI with:
> *"Here is my phone dataset: [paste table]. Tell me: (1) the price range per target_segment, (2) which spec varies most across segments, (3) any pattern that surprises you."*
Write down the 3 answers — you'll reference them in your presentation.

**6. Feature engineering — normalize specs into comparable scores**
Raw specs (camera_mp, battery_mah, etc.) aren't directly comparable. Convert each phone into four 0–10 scores: `camera_score`, `performance_score`, `battery_score`, `value_score`. Prompt:
> *"Convert this phone dataset into normalized 0–10 scores for camera, performance, battery life, and value-for-money, based on the raw specs. Show your scoring logic, not just the numbers."*

**7. Define your personas (3–4, in writing)**
For each persona, list which of the four scores matters most. Example:
| Persona | camera weight | performance weight | battery weight | value weight |
|---|---|---|---|---|
| Priya (photography) | 0.5 | 0.1 | 0.2 | 0.2 |
| Arjun (gaming) | 0.1 | 0.5 | 0.3 | 0.1 |

Weights per persona must add up to 1.0.

**8. Build the Weighted Sum Model (WSM) — the actual recommendation logic**
For each phone, multiply its 4 scores by the persona's 4 weights and add them up:
> `match_score = (camera_score × camera_weight) + (performance_score × performance_weight) + (battery_score × battery_weight) + (value_score × value_weight)`

Worked example — Priya (camera weight 0.5) looking at a phone scoring camera=9, performance=6, battery=7, value=5:
> `match_score = (9×0.5) + (6×0.1) + (7×0.2) + (5×0.2) = 4.5 + 0.6 + 1.4 + 1.0 = 7.5`

Run this for every phone × every persona. Highest score = top recommendation for that persona.

**9. Build the recommender UI (vibe coding)**
"Vibe coding" means describing the interface you want in plain English and iterating with GenAI rather than hand-writing every line. Prompt:
> *"Build a simple Python Jupyter widget (or a basic HTML page) where a user selects a persona from a dropdown and sees the top 3 recommended phones with their match scores and one sentence explaining why each was picked."*
Iterate: run it, screenshot what's wrong, paste the screenshot/description back and ask for fixes.

**10. Prepare your presentation**
Must include: your 3–4 personas, your WSM formula with one worked example, a screenshot of the working UI, and the 3 EDA findings from Step 5.

### Ties back to Chapters 1–4
- Prompt design for persona definitions and scoring logic → **Ch.2** (6-element prompt structuring: be specific about role, format, constraints in every prompt above)
- Choosing how to apply a foundation model to a recommendation task vs. a generation task → **Ch.3**
- Building the UI itself → **Ch.1** vibe coding practice

---

## PJ2 — Wellness Dashboard

**Samsung context:** Samsung Health + Web Dashboard Development

**Scenario:** You're prototyping a feature for the Samsung Health app: a weekly wellness dashboard that turns raw fitness-tracker numbers into a friendly summary with coaching advice, for one sample user.

**Outcome:** An interactive dashboard showing one week of health metrics, 3 charts, and personalized coaching messages.

### Step-by-step

**1. Set up Anaconda + Jupyter** (same as PJ1, Step 1)

**2. Understand the wearable/health-tracking landscape**
Skim how Samsung Health, Fitbit, and Apple Health present weekly summaries (steps, sleep, heart rate, stress) — you're building something in that spirit, scaled down to one user, one week.

**3. Generate your sample user's data**
Your persona is **Emily Park, 29, moderately active office worker.** Paste into Gemini:
> *"Generate 7 days of realistic fitness-tracker data for a moderately active 29-year-old office worker named Emily Park. Include: date, steps, sleep_hours, resting_heart_rate, stress_score (0–100), active_minutes. Make it realistic — weekdays lower activity than weekends, one bad-sleep night, one high-stress day."*

**4. Explore the data (EDA)**
> *"Here is Emily's 7-day data: [paste]. Identify: (1) her best and worst day for stress, (2) any correlation you notice between sleep and next-day steps, (3) one thing she should be proud of this week."*

**5. Calculate weekly summary metrics**
By hand or with a short prompt, compute: average steps/day, average sleep, average resting heart rate, total active minutes, and the day with the highest stress score. These numbers are what the dashboard will display as headline stats.

**6. Draw three weekly charts**
Minimum: (a) a line chart of steps per day, (b) a bar chart of sleep hours per day, (c) a chart of your choice (stress trend or active minutes). Ask GenAI to generate the plotting code:
> *"Write Python matplotlib code to plot: a line chart of daily steps, a bar chart of daily sleep hours, and a line chart of daily stress score, for this data: [paste]."*

**7. Research national/general wellness benchmarks**
> *"What is the generally recommended daily step count and sleep duration for an adult office worker? Give me 2–3 benchmark numbers I can compare Emily's week against, with sources if possible."*
Note: treat GenAI's benchmark claims as a starting point, not gospel — this is exactly the kind of factual claim Day 4 taught you to verify, not accept blindly.

**8. Design coaching messages**
Write 2–3 short, personalized coaching messages based on Emily's actual data (not generic advice). Prompt:
> *"Based on this week's data — [paste summary stats] — write 3 short, encouraging coaching messages (1–2 sentences each) a wellness app would show Emily. Reference her actual numbers, not generic fitness advice."*

**9. Build the dashboard layout (vibe coding)**
> *"Build a simple HTML/CSS dashboard page showing: Emily's name and week, 3 headline stat tiles (avg steps, avg sleep, avg stress), the 3 charts from Step 6 as images, and the 3 coaching messages from Step 8."*

**10. Prepare your presentation**
Must include: the 3 charts, the 3 coaching messages with the data point each one is based on, and one honest note on where GenAI's output needed correcting (a wrong benchmark, an awkward chart, etc.) — this ties directly to Day 4's reliability lessons.

### Ties back to Chapters 1–4
- Generating coaching messages and researching benchmarks → **Ch.2** prompt engineering (specificity, grounding in real data)
- Choosing the right foundation model for data analysis vs. content generation → **Ch.3**
- Treating GenAI's benchmark/factual claims with the same scrutiny as Day 4's hallucination content → **Ch.4**
- Dashboard layout build → **Ch.1** vibe coding practice

---

## PJ3 — IoT Energy-Saving Assistant

**Samsung context:** SmartThings / Assistant UI

**Scenario:** You're prototyping a SmartThings feature: an assistant that looks at a household's raw appliance-usage data and gives energy-saving advice through simple automation rules.

**Outcome:** An assistant UI (built in Gemini Canvas) that shows energy-saving rules and generated advice for a sample household.

**⚠ Requires Gemini Canvas specifically** — if you're not on Gemini, flag this with your instructor before you start; the Canvas step may not transfer to another tool.

### Step-by-step

**1. Set up Anaconda + Jupyter** (same as PJ1, Step 1)

**2. Understand IoT and home automation basics**
An automation "rule" is a simple if-this-then-that statement: *"IF living room is empty for 10+ minutes AND lights are on, THEN turn off lights."* You'll be designing rules like this, not writing IoT firmware.

**3. Warm-up: sketch automation logic on paper first**
Before touching data, write 3 if-then rules you'd want in your own home (e.g., AC schedule, standby power for TV, water heater timing). This primes you for Step 7.

**4. Generate your household's raw IoT dataset**
> *"Generate 7 days of hourly appliance energy usage (in watts) for a 3-bedroom household with these devices: AC, refrigerator, washing machine, TV, water heater, lights. Make it realistic — AC usage spikes in afternoon, washing machine runs twice a week, fridge is constant baseline, lights peak in evening."*

**5. Explore the data (EDA)**
> *"Here is the household's hourly usage data: [paste]. Identify: (1) which appliance uses the most energy overall, (2) any hours where multiple appliances peak simultaneously (a wasteful overlap), (3) one clearly avoidable usage pattern."*

**6. Design your energy-saving rules**
Turn your Step 3 sketch plus the Step 5 findings into 4–5 concrete if-then rules, each tied to an actual pattern in your data. Example: *"IF AC and water heater both peak between 2–4pm, THEN stagger water heater to run after 6pm."*

**7. Test rules and generate advice (in Gemini)**
> *"Given this household's usage data [paste] and these automation rules [paste your rules], write 3 short pieces of advice a SmartThings app would show the homeowner this week, each referencing a specific number from their data (e.g. potential kWh or % saved)."*

**8. Build the assistant UI in Gemini Canvas**
> *"Build a simple assistant UI in Canvas showing: a weekly energy usage summary, the 4–5 automation rules as toggle cards, and the 3 pieces of generated advice from Step 7."*
Iterate inside Canvas — this tool is built for exactly this kind of prompt-and-refine UI generation.

**9. Prepare your presentation**
Must include: your 4–5 rules with the data pattern each one addresses, a screenshot of the Canvas UI, and the 3 pieces of generated advice with their supporting numbers.

### Ties back to Chapters 1–4
- Testing rules and generating advice via structured, verifiable prompts → **Ch.2**
- Choosing Gemini/Canvas specifically for this use case, understanding why a general chat model alone wouldn't build a UI → **Ch.3** platform comparison and selection
- Assistant UI build → **Ch.1** vibe coding practice
- Note: this is the one project that specifically requires Gemini Canvas — if you're on another platform, flag this early with your instructor.

---

## PJ4 — New Product Marketing Page

**Samsung context:** Samsung.com / Branding & Marketing Webpage

**Scenario:** Samsung is launching a new (fictional, but plausible) product feature. You're the one-person marketing+dev team building the promotional web page from concept to finished page.

**Outcome:** A web page with AI-generated copy and images promoting a Samsung product you define.

### Step-by-step

**1. Review AI usage principles first**
Before generating any marketing content or images, re-read Day 4's notes on unauthorized use, copyright, and brand misuse — you're about to generate promotional content that mimics a real brand's voice, which is exactly the scenario those principles were written for.

**2. Define your product**
Pick a plausible new Samsung product or feature — real or invented but realistic (e.g., "Galaxy Buds with real-time sign-language translation" or "a Neo QLED TV with AI pet-monitoring mode"). Write 2–3 sentences describing what it does and who it's for.

**3. Craft the marketing concept brief with GenAI**
> *"I'm marketing a new Samsung product: [paste your 2–3 sentence description]. Write a one-paragraph marketing concept brief covering: target audience, key selling point, and emotional hook, in Samsung's typical clean/premium brand voice."*

**4. Understand essential web page components**
A marketing page needs, at minimum: a hero headline + image, 3 feature callouts with short copy, one customer-benefit section, and a call-to-action. Plan your page around these five blocks before generating anything.

**5. Analyze real brand marketing benchmarks**
Look at 2 real samsung.com or apple.com product pages. Note: how long are their headlines? How many words per feature callout? What's the ratio of image to text? Write down 3 concrete observations — you'll be graded partly on whether your page matches this real-world pattern, not just on creativity.

**6. Generate marketing copy for each section**
> *"Using this concept brief [paste from Step 3] and this page structure [hero/3 features/benefit section/CTA], write the actual copy for a Samsung product page: one headline (under 8 words), one hero subtext (1 sentence), 3 feature callouts (15–20 words each), one benefit paragraph (2–3 sentences), one CTA button label (2–4 words)."*

**7. Generate supporting images**
Use Gemini's image generation (or Stable Diffusion) for the hero image and any product visuals:
> *"Generate a clean, premium product photography-style image of [your product], on a minimal light background, in Samsung's typical product photography style."*
Generate 2–3 variants and pick the best — don't settle for the first output.

**8. Build the web page (vibe coding)**
> *"Build an HTML/CSS page using this copy [paste Step 6] and this image [describe/attach Step 7], following the hero/3-features/benefit/CTA structure. Clean, minimal, Samsung-style layout."*

**9. Enhance layout and visual flow**
Compare your page against your Step 5 benchmark notes. Ask GenAI to specifically tighten spacing, adjust font sizing, or fix any section that doesn't match the "premium/clean" pattern you observed in real Samsung/Apple pages.

**10. Conduct a review pass with GenAI**
> *"Review this marketing page copy and layout [describe/paste] as if you were a Samsung brand reviewer. Flag anything that sounds off-brand, any claim that isn't substantiated, or any copyright/trademark risk (e.g. referencing a competitor by name)."*
This step is a direct application of Day 4 — treat the review output as a real pre-publication check, not a formality.

**11. Prepare your presentation**
Must include: your product definition, the finished page (screenshot or live), your 3 real-brand benchmark observations and whether you matched them, and one thing the Step 10 review caught that you fixed.

### Ties back to Chapters 1–4
- Concept brief and page copy → **Ch.2** prompt engineering (structuring for tone/style/constraints)
- Generating and reviewing images/content responsibly, avoiding unauthorized brand mimicry → **Ch.4**
- Page build → **Ch.1** vibe coding, image/code generation models

---

## Before You Start — Checklist

- Anaconda + Jupyter installed and working (PJ1, PJ2, PJ3)
- Gemini account ready (free tier is sufficient for all four projects)
- Google account for SSO, if needed
- Review your Ch.1–4 notes on prompt structuring, model selection, and Responsible AI — every project above expects you to apply them at named points, not just execute steps
- Decide which topic you're choosing **before** Day 5 morning if possible — you'll move faster if you've already skimmed your topic's steps once
