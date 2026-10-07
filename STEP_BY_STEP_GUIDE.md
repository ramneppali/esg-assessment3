# Step-by-Step Guide: How to Complete Assessment 3

Work in this order: Q1, then Q4, then Q3, then Q2, then the final pass. Q1 and Q4 need the most hands-on work. Save every screenshot in a `screenshots/` folder as you go, and name each one (for example `q1_intents.png`).

---

## Step 0. Setup

1. Create a GitHub account if you do not have one, then create a new repository named `esg-assessment3`.
2. Upload this folder's contents (README, `q3/`, `q4/`, `report/`).
   - In the browser: **Add file**, then **Upload files**.
   - Or in a terminal: `git init`, `git add .`, `git commit -m "Initial"`, `git remote add origin <url>`, `git push -u origin main`.
3. Open **Settings**, then **General**, and confirm the repo is public (or add the teaching team as collaborators).
4. Open the brief ("ASSIGN 3.pdf") next to `report/Assessment3_Report.md`.

---

## Step 1. Q1: Build the Dialogflow CX chatbot

### 1.1 Create the project and agent

1. Go to https://console.cloud.google.com and sign in.
2. Create a new project named `esg-chatbot`.
3. Open **APIs & Services**, then **Library**, search **Dialogflow API**, and click **Enable**.
   - If asked for billing, add it. New accounts get free trial credit and this prototype is very small. Delete the project afterwards.
4. Go to https://dialogflow.cloud.google.com/cx and select your project.
5. Click **Create agent** and set:
   - Display name: `ESG Incident Assistant`
   - Location: `global` (or your nearest region)
   - Time zone: your local time zone
   - Default language: English
6. Screenshot the new agent.

### 1.2 Create the entities

1. Open **Manage**, then **Entity types**, then **Create**.
2. Entity `incident_type` (kind: Map). Add these values and synonyms:

| Value | Synonyms |
|---|---|
| water_leak | water leak, leak, burst pipe, dripping tap, flooding, pipe burst |
| energy_waste | energy waste, lights left on, aircon on, air conditioning running, heater on |
| waste_contamination | recycling contamination, wrong bin, contaminated bin, overflowing bin |
| unsafe_disposal | unsafe disposal, chemical dumped, hazardous waste, dumped waste |
| accessibility_barrier | blocked entrance, blocked ramp, lift broken, accessibility problem |

3. Entity `yes_no` (kind: Map): `yes` with synonyms (yes, yeah, yep, still happening, ongoing, sure); `no` with synonyms (no, nope, stopped, not anymore).
4. Screenshot the entity list and one entity.

### 1.3 Create the intents

1. Open **Manage**, then **Intents**, then **Create**.
2. Create these five intents. Add 8 to 10 training phrases each. The report has starter phrases; add more of your own, including informal and misspelt ones.
   - `report_incident`
   - `report_hazard_urgent`
   - `ask_what_can_you_do`
   - `request_human`
   - `check_ticket_status`
3. Screenshot the intents list and the training phrases of two intents.

### 1.4 Build the pages and routes

1. Open **Build**, then **Start** (the Default Start Flow).

**Start page**

1. Click the **Start** page.
2. Under **Entry fulfillment**, add the agent say message:
   *"Hi, I'm the ESG Incident Assistant, an automated bot. I can help you report sustainability issues. Please don't include personal details. A person reviews every report. What would you like to do?"*
3. Under **Routes**, add intent routes:
   - `report_incident` goes to the page Collect Incident Details
   - `report_hazard_urgent` goes to Collect Incident Details
   - `ask_what_can_you_do`: fulfilment message listing the five functions, then stay on page
   - `request_human` goes to Human Handoff
   - `check_ticket_status`: message saying ticket tracking is not in this prototype and to contact the sustainability team

**Collect Incident Details page** (click **+** next to Pages)

1. Under **Parameters**, add four parameters and mark all as **Required**:

| Display name | Entity type | Prompt (agent says) | Re-prompt |
|---|---|---|---|
| incident_type | @incident_type | Which type of issue is it? Water leak, energy waste, waste problem, unsafe disposal or accessibility barrier? | Please choose one of: water leak, energy waste, waste problem, unsafe disposal, accessibility barrier. |
| location | @sys.any | Where is it? Please give the building and area. | Sorry, which building and area is it in? |
| ongoing | @yes_no | Is the problem still happening right now? | Please answer yes or no. Is it still happening? |
| anonymous | @yes_no | Would you like your name on this report? Say no to stay anonymous. | Please answer yes or no. |

2. Add a route with condition `$page.params.status = "FINAL"` that goes to Triage.

**Triage page**

1. Add a route with condition: `$session.params.ongoing = "yes" AND $session.params.incident_type IN ("water_leak", "unsafe_disposal")` going to Hazard Escalation.
2. Add a second route with condition `true` going to Standard Logging.

**Hazard Escalation page**

1. Entry fulfilment: *"This could cause damage or harm, so I have notified the facilities duty team now. Please keep clear of the area. Your reference is ESG-0001. A person will follow up."*
2. Add a route (condition `true`) to End Session.

**Standard Logging page**

1. Entry fulfilment: *"Thank you. Your report has been logged. Your reference is ESG-0002. The sustainability team will review it within 3 working days."*
2. Add a route (condition `true`) to End Session.

**Human Handoff page**

1. Entry fulfilment: *"No problem. I'm passing this to a person. Please contact the sustainability team at [team contact]. I have noted your conversation so you do not have to repeat yourself."*
2. Add a route (condition `true`) to End Session.

### 1.5 Add fallback and no-input handling

1. On the Collect Incident Details page, open **Event handlers**.
2. Add `sys.no-match-default`. Add three conditions, each with its own message:
   - 1st time: *"Sorry, I didn't catch that. Could you describe the issue in a few words?"*
   - 2nd time: *"Which of these is closest? Water leak, energy waste, waste problem, unsafe disposal, accessibility barrier."*
   - 3rd time: transition to Human Handoff
3. Add `sys.no-input-default` with a re-ask message, then a transition to Human Handoff on the second occurrence.
4. Repeat on the Start page.
5. Screenshot the event handlers.

### 1.6 Test

1. Click **Test Agent** (top right).
2. Run Transcript 1 from the report (water leak, ongoing, anonymous). Confirm it reaches Hazard Escalation.
3. Run Transcript 2 (unclear input twice, then energy waste, ongoing = no). Confirm it reaches Standard Logging.
4. Test `request_human` by typing "talk to a person".
5. Fix any issues, then screenshot each finished conversation.

### 1.7 Screenshots checklist

- [ ] Flow visualiser with every page and route
- [ ] Intent list and training phrases
- [ ] Entity with synonyms
- [ ] Form parameters
- [ ] Triage condition route
- [ ] Fallback handlers
- [ ] Both test conversations

### 1.8 Record the video (under 2 minutes)

1. Open the timed script in Q1(e) of the report.
2. Record your screen and voice (QuickTime: **File**, then **New Screen Recording**; or Teams).
3. Rehearse once, then record. Aim for about 100 seconds.
4. Upload it to Microsoft Stream and set the sharing so the teaching team can view it.
5. Paste the link in the report and test it in a private window.

### 1.9 Write the report section

1. Replace each `[TODO]` in Q1 with your screenshots and your own transcripts.
2. Redraw the conversation map in draw.io, or paste a screenshot of the flow visualiser.
3. Add 2 to 3 sentences on what you learned and what you would improve.

---

## Step 2. Q4: NotebookLM experiments

1. Choose 3 to 4 public ESG documents (for example AASB S2, a GRI standard, one company sustainability report). Record title, publisher, year and URL in `q4/experiment_log.md`.
2. Go to https://notebooklm.google.com, create a notebook and upload the documents. Screenshot the sources panel.
3. Run each feature in turn:

| Feature | How to run |
|---|---|
| Source-grounded chat | Ask 3 to 4 specific questions. Example: "What must entities disclose about transition plans?" |
| Briefing / summary | Use the Studio panel or ask for a one-page briefing for an ESG workshop |
| Audio Overview | Generate it and listen to it. Note the length and what it left out |
| Mind map | Generate it and check the links between topics |
| Quiz / flashcards | Generate it and check questions against the source |
| Notes | Save a response as a note and re-check it |

4. For each output, copy the exact prompt and take a screenshot.
5. Check accuracy: pick 10 claims from the output, find the matching passage in the source, and mark each correct, partly correct, unsupported or wrong. Use the table in the log.
6. Click each citation and check whether it supports the claim.
7. Score usefulness 1 to 5, and write one example of a limitation (omission, hallucination, bias, oversimplification).
8. Fill the summary table in the log, then transfer it into Q4(c) of the report.
9. Write the conclusion: when students should use it, when they should not, and what rules a university should set (verification, acknowledgement, privacy).
10. Commit the log and screenshots to GitHub.

---

## Step 3. Q3: LLM triage experiment

### 3.1 Install an LLM (free, local option)

1. Install Ollama from https://ollama.com.
2. In a terminal: `ollama pull llama3.1:8b`.
3. Check it runs: `ollama run llama3.1:8b "hello"`, then exit.
   - If your computer is slow, use an API model instead. Set `LLM_BASE_URL`, `LLM_MODEL` and `LLM_API_KEY` as in the README. Never commit keys.

### 3.2 Run the experiment

```bash
cd esg-assessment3/q3
export LLM_BASE_URL=http://localhost:11434/v1
export LLM_MODEL=llama3.1:8b
python3 triage.py --modes rules,llm
```

1. Optional zero-shot baseline: `pip install -r requirements.txt`, then `python3 triage.py --modes rules,llm,zeroshot`. The first run downloads a large model.
2. Optional: run the original prompt for contrast with `python3 triage.py --modes llm --prompt prompt_v1_original.txt`. Copy the results first, because they overwrite `results/llm_results.json`.
3. Run the LLM mode 2 to 3 times and compare, to check consistency.

### 3.3 Write up

1. Q3(a): paste the JSON for M1, M2 and M3 from `results/llm_run_log.jsonl`, and list how the revised prompt differs from the original.
2. Q3(b): add the LLM and zero-shot rows to the comparison table. Write 3 to 4 sentences on:
   - where the methods agree and disagree
   - which got M2 right
   - whether results were consistent between runs
   - any invalid JSON from the LLM (`_schema_problems`)
   - any sign of bias, with the caution that 5 messages is too few to prove it
3. Q3(c): keep or edit the improvements and readiness paragraph so it matches what you saw.
4. Q3(d): redraw the Azure architecture in draw.io, and explain each component in your own words.
5. Commit `results/` to GitHub.

---

## Step 4. Q2: Cloud security incident

1. Read these two sources: the Mandiant blog post on UNC5537 and Snowflake's customer security guidance.
2. Check every fact in Q2(a): dates, victim names, the number of affected organisations, the cause and what data was taken.
3. Find the AT&T disclosure (SEC Form 8-K) and add its URL, or remove that claim.
4. Redraw the Q2 diagram in draw.io.
5. For Q2(b), confirm the SaaS / IaaS statements against Snowflake's documentation.
6. Reword everything in your own words and add the Snowflake guidance to the references.

---

## Step 5. Final pass

1. Search `Assessment3_Report.md` for `[TODO]` and resolve all of them.
2. Insert the screenshots into the Word version. Run `python3 report/build_docx.py` first, then edit the .docx.
3. Replace the text diagrams with draw.io images.
4. Check formatting: headings, page numbers, table of contents if the brief asks for one, APA references.
5. Read the brief one last time and tick every box in the README checklist.
6. Complete the AI acknowledgement on the LMS. State what you used AI for and what you checked yourself.
7. Test every link in a private browser window (Stream video and GitHub repo).
8. Submit before 11:59 pm AEDT on 13 October, and keep a copy of the confirmation.

---

## Common mistakes to avoid

- Screenshots without explanation. Always say what the screenshot shows and why.
- Describing tools without linking them to an ESG decision or outcome.
- Invented or unverified results. Marks go to evidence.
- Missing privacy or ethics detail. Name the specific risk and the fix.
- Broken links or a private repo or video.
- Leaving draft wording unchanged. Rewrite it so it is your own work.
