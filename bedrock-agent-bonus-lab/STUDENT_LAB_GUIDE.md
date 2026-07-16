# Bonus Lab: Build a Real AI Agent on Amazon Bedrock

**Duration:** ~60 minutes
**What you'll do:** Analyze real customer feedback with Claude on Bedrock, then build your own AI agent — **Course Copilot** — an assistant that answers questions about your own Generative AI course material by retrieving real content from the course chapters, not guessing.

---

## Before you start

1. You've been given an IAM username/password for this AWS account. Log in at the console URL provided, and set a new password when prompted.
2. Set your region to **US East (N. Virginia) — us-east-1** in the top-right region selector. Everything in this lab only exists in that region.

---

## Part A — Grounded Prompting (20 min)

Toy prompts like "write me a poem" don't teach you much. Instead, you'll use Claude to do real analytical work on real (anonymized) customer feedback.

1. Go to **Amazon Bedrock → Playgrounds → Chat**.
2. Choose model: **Anthropic Claude 3 Haiku**.
3. Paste the customer reviews below into the chat, followed by your instructions.

**Sample data — paste this in first:**

```
1. "Delivery took 6 days when the site promised 2. Product itself was fine."
2. "App keeps crashing when I try to apply a coupon code at checkout."
3. "Customer support resolved my refund in 10 minutes over chat — excellent."
4. "The size chart is wrong for hoodies, I had to return twice to get the right fit."
5. "Great quality for the price, will order again."
6. "Tracking link never updates, I had no idea where my order was for a week."
7. "Checkout page froze twice before payment finally went through."
8. "Packaging was damaged but the item inside was okay."
9. "Loved the product but the invoice email never arrived, needed it for reimbursement."
10. "Support was rude and unhelpful when I asked about a late delivery."
```

**Then ask Claude (as one prompt):**

```
You are a customer experience analyst. Based on the 10 reviews above:
1. Classify each review as Positive, Negative, or Mixed.
2. Identify the top 3 recurring complaint themes (not just symptoms — the underlying cause).
3. For each theme, recommend one concrete fix a small e-commerce team could ship this sprint.
4. Output as a markdown table for (1), then a short bulleted list for (2) and (3).
```

**Try this next** — change ONE thing and compare the output:
- Add to your prompt: `Assume the team only has capacity to fix ONE thing this sprint — which one, and why?`
- Re-run with **Claude 3 Sonnet** instead of Haiku. Compare quality vs. speed.

This is the same skill — structured prompting for a real decision — that shows up in any job using an LLM: you're not asking for text, you're asking for a decision-ready output.

---

## Part B — Build the Course Copilot Agent (35 min)

You'll build this step-by-step with the trainer. A Knowledge Base has already been created and loaded with the 4 Generative AI course chapters — you're building the agent that uses it, not the knowledge base itself.

### Step 1 — Create the agent

1. Go to **Amazon Bedrock → Agents → Create Agent**.
2. Name it `genai-agent-<yourusername>` (e.g. `genai-agent-student03`).
3. Under **Agent resource role**, choose **Use an existing service role** and select `BedrockAgentLabExecutionRole`.
4. Select model: **Anthropic Claude 3 Haiku**.
5. Paste this into **Instructions for the Agent**:

```
You are Course Copilot, an assistant for a Generative AI course covering:
Introduction to Generative AI, Prompt Engineering Basics, Foundation Models and
Platforms, and AI Ethics and Responsibility.
Answer questions using the course knowledge base. If the knowledge base doesn't
contain the answer, say so clearly instead of guessing.
Keep answers concise and cite which chapter the answer came from when you can.
```

### Step 2 — Attach the Knowledge Base (this is what makes it an *agent* grounded in real content, not a generic chatbot)

1. Scroll to **Knowledge bases → Add**.
2. Select the existing knowledge base: `genai-course-kb`.
3. In **Knowledge base instructions for Agent**, enter:
   ```
   Use this knowledge base to answer any question about Generative AI concepts,
   prompt engineering, foundation models, or AI ethics covered in the course.
   ```
4. Save.

### Step 3 — Prepare and test

1. Click **Prepare** (top right) to build the agent.
2. In the test chat pane on the right, try:
   - `What is Generative AI and how is it different from traditional AI?`
   - `Give me 3 prompt engineering techniques from the course, with an example of each.`
   - `What foundation model platforms were discussed?`
   - `What are the main AI ethics and responsibility concerns covered in the course?`
   - `What's the capital of France?` (see how it handles a question outside the knowledge base)

### What to notice

- You never pasted any course content into the agent — it retrieved the relevant passage from the actual PDF chapters at answer time and grounded its response in that, not in what Claude already "knew."
- Ask it something outside the 4 chapters and watch it say so, instead of confidently making something up — that's the difference between a knowledge base-grounded agent and a plain chatbot.
- This same pattern — an LLM + retrieval over your own documents — is how real "chat with your data" systems are built: internal wikis, policy documents, support knowledge bases, and beyond. You just built the same shape of system, pointed at your own course material.

---

## Cleanup note

Everything in this lab (your agent, the IAM account, the knowledge base) is temporary and will be removed after today. Take screenshots of your working agent if you want to keep a record.
