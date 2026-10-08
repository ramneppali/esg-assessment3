# Q4 NotebookLM experiment log

Complete this as you run each experiment. Keep screenshots in `q4/screenshots/` and reference them here.

## Test setup

| Item | Value |
|---|---|
| Date tested | 7 October 2026 |
| NotebookLM plan / version | Product name shown in the app footer: "Gemini Notebook" (the assessment calls it NotebookLM). Notebook title: "BUS5001 A3 Q4 – ESG Climate Disclosure Sources". Studio panel options seen: Audio Overview, Video Overview, Slide Deck, Mind Map, Reports, Flashcards, Quiz, Infographic, Data Table. Plan used: free, personal Google account. |
| Usage limits notice (in-app, copied) | Limits refresh every 5 hours instead of every 24 hours. Per-feature limits are replaced by one flexible notebook-level limit. When out of limits, generation of videos, slides and similar items can be deferred to a background queue. |
| Scenario | A student preparing an ESG briefing on climate-related disclosure, using two standards, one framework standard and one company report |
| Sources uploaded (title, publisher, year, URL) | (1) AASB S2 Climate-related Disclosures, Authorised Version F2024L01472, AASB, 2024, 59 pp, https://standards.aasb.gov.au/ (file `AASBS2_09-24.pdf`). (2) IFRS S2 Climate-related Disclosures, IFRS Foundation / ISSB, June 2023, 46 pp (file `issb-2023-a-ifrs-s2.pdf`). (3) GRI 305: Emissions 2016, Global Reporting Initiative, 26 pp (file `GRI 305_ Emissions 2016.pdf`). (4) FY25 Environmental, Social and Governance Report, NEXTDC Limited, 1 July 2024 to 30 June 2025, 44 pp, https://nextdc.com/hubfs/ASX%20Announcements/FY25%20Environmental%2C%20Social%20and%20Governance%20Report.pdf (file `FY25 Environmental, Social and Governance Report.pdf`). |

## Prompt pack (run these, then record the real outputs below)

Use the same sources for every feature. Copy the prompt text exactly into NotebookLM, and keep every output unedited. If you change a prompt, record the changed version, not this one.

| # | Feature | Prompt or action | What to capture |
|---|---|---|---|
| 1 | Source-grounded chat | "What do these sources require or recommend that an organisation discloses about its climate transition plan? Answer in 8 to 10 short bullet points and cite the source for each." | Full answer with citation markers, plus a screenshot of one citation opened |
| 1b | Chat limit test | "What does the company report say about its Scope 3 emissions target for 2030?" (choose a question whose answer is NOT in your sources) | Whether it says the sources do not contain this, or invents an answer |
| 2 | Briefing document | Studio panel, Report, Briefing doc. Add the instruction: "Write a one-page briefing for a student workshop on climate-related disclosure, with a key terms list." | The document and a screenshot |
| 3 | Audio Overview | Studio panel, Audio Overview, generate. Optionally customise: "Focus on what the standards require, for a first-year student." | Screenshot of the player, generation time, and a transcript of 10 claims you heard |
| 4 | Mind map | Studio panel, Mind map, generate | Screenshot of the map, and 10 of its nodes or links checked against the sources |
| 5 | Quiz and flashcards | Studio panel, Quiz and Flashcards, generate with 10 questions | Screenshot, and 10 questions checked for a correct answer key |
| 6 | Notes | Save the chat answer from #1 as a note, then try "Convert to source" | Screenshot, and whether the note keeps the citations |

Pick claims for the accuracy tables below from the unedited outputs, and check each against the page of the original document. For #3 and #4 the claims are what you heard or saw, since there is no text to quote.

Privacy check (done 7 October 2026, accessed by fetching the page text; the tool is now named "Gemini Notebook" and old NotebookLM help links redirect to it):

- **Page:** "Privacy and Terms of Use in Gemini Notebook", https://support.google.com/gemininotebook/answer/17004255 (also checked "Learn about Gemini Notebook", https://support.google.com/gemininotebook/answer/16164461, section "Learn how Gemini Notebook protects your data").
- **What it says:** Files you add, outputs you generate and your chat history are used to build your knowledge base and assist you. Content "will not be used to directly train our foundational AI models, unless you choose to provide feedback". If you give thumbs up or down feedback, the related prompts, sources, uploads and outputs are collected, reviewed by specially trained teams (disconnected from your Google Account first), used to improve Google products and machine-learning technologies, and kept for up to 3 years. For Google Workspace and Workspace for Education users, uploads, queries and responses are not reviewed by human reviewers and are not used to train AI models, even with feedback. Data shared with other Google services (for example the Gemini app) follows the Google Privacy Policy. The page also tells users to respect copyright and not to include confidential or sensitive information in feedback.
- **Plan and account used:** Free plan, personal Google account (student confirmed). The Google Terms of Service apply, not the Workspace terms, so the no-human-review rule for Workspace accounts does not cover this use.
- **Did you press thumbs up or down on any output?** No (student confirmed), so none of the content was sent to Google as feedback and, per the page, it was not used to directly train Google's foundation models.
- **Implication for this task:** The four uploaded files are public reports and standards, not confidential, but they are third-party copyrighted material, so the PDFs are kept out of the GitHub repository. For real work, confidential client or company documents should not be uploaded to a free personal account.

## Experiment template (copy one per feature)

### Feature: [name]

- **Prompt / action:** [exact text]
- **Output summary:** [what it produced]
- **Screenshot:** `screenshots/[file].png`
- **Accuracy check (10 claims):**

| # | Claim from output | Source passage / page | Verdict (correct / partly / unsupported / wrong) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

- **Citation check:** [how many citations really support the statement]
- **Accuracy score:** [x/10]
- **Usefulness (1 to 5) and why:** [..]
- **Limitations observed (bias, hallucination, missing content, over-reliance):** [..]
- **Time saved vs doing it manually:** [..]

## Recorded experiments

### Feature 1: Source-grounded chat (7 October 2026)

- **Prompt / action:** "What do these sources require or recommend that an organisation discloses about its climate transition plan? Answer in 8 to 10 short bullet points and cite the source for each." All four sources selected.
- **Output summary:** Nine bullets with numbered citations (1 to 14). Citations 1 to 8 point to `AASBS2_09-24.pdf` and `issb-2023-a-ifrs-s2.pdf`; bullet 8 also cites `GRI 305_ Emissions 2016.pdf` (11); bullet 9 cites `FY25 Environmental, Social and Governance Report.pdf` (13, 14). The answer ended with an unrequested offer of a comparison table of IFRS S2, AASB S2 and GRI emissions rules.
- **Screenshot:** `screenshots/q4_prompt1_chat.png` shows the answer with citation markers and an opened citation (AASB S2, para 36(e), planned use of carbon credits; supports claims 8a and 8b).
- **Status:** [TODO: confirm you opened each page below and agree with each verdict. The verdicts are a first pass.]
- **Accuracy check (10 claims; PDF page numbers):**

| # | Claim from output | Source passage / page | Verdict |
|---|---|---|---|
| 1 | Transition plan is part of overall strategy and lays out targets, actions or resources for a lower-carbon transition | AASB S2 p.16, defined term "climate-related transition plan" | Correct |
| 2 | Disclose key assumptions and dependencies | AASB S2 p.9, para 14(a)(iv) | Correct |
| 3 | Business model and resource allocation changes, including decommissioning, capex and R&D | AASB S2 p.9, para 14(a)(i) | Correct |
| 4 | Direct actions such as retrofitting equipment, altering production processes, facility relocations, workforce adjustments | AASB S2 p.9, para 14(a)(ii): "changes in production processes or equipment, relocation of facilities, workforce adjustments" | Partly: the word "retrofitting" is not in the standard |
| 5 | Indirect efforts through customers and supply chains | AASB S2 p.9, para 14(a)(iii) | Correct |
| 6 | Quantitative and qualitative information on resourcing | AASB S2 p.9, para 14(b) | Correct |
| 7 | Progress against plans from previous periods | AASB S2 p.9, para 14(c) | Correct |
| 8a | Explain reliance on carbon credits or offsets to achieve targets | AASB S2 p.15, para 36(e)(i); GRI 305 p.8, requirement 1.1 (type, amount, criteria or scheme of offsets) | Correct |
| 8b | Third-party verification schemes, offset types and permanence assumptions | AASB S2 p.15, para 36(e)(ii) to (iv) | Correct. Permanence is in AASB S2, not GRI 305. |
| 9 | "In corporate practice, transition plans outline specific decarbonisation pathways, operational boundaries and investment levers contingent on established net zero targets" | NEXTDC p.28: the company is "exploring" a net zero target and will "develop a supporting Climate Transition Plan, contingent on the targets set" | Partly: one company's future plan is presented as general corporate practice, and it is not a requirement of any source |

- **Citation check:** Citations 1 to 8 pointed to the correct standards. [TODO: confirm the IFRS S2 pages for citations 2, 4, 6, 8 and 12 by opening them.] Citations 13 and 14 pointed to NEXTDC, which supports the wording but not the generalisation.
- **Accuracy score:** 8 of 10 fully correct, 2 partly correct, 0 wrong.
- **Generation time:** about 1 minute (student). Student's view: good.
- **Usefulness (1 to 5) and why:** 4 out of 5. Fast, cited answer, and 8 of 10 claims fully correct. The citations let me check each claim against a page. It loses a point for the overgeneralised bullet 9 and the heavy reliance on AASB S2.
- **Limitations observed (bias, hallucination, missing content, over-reliance):** The answer relied almost entirely on AASB S2 and IFRS S2, which have near-identical wording, so it did not show that two standards were consulted. GRI 305 added nothing on transition plans, and the answer did not warn that GRI 305 will be superseded by GRI 102 from 1 January 2027 (GRI 305 p.1). Bullet 9 turned one company's intention into a general statement. The question asked what is required or recommended, but bullet 9 is neither. An unrequested follow-up offer was appended.
- **Time saved vs doing it manually:** about 25 minutes (estimate, not measured). Finding and writing nine cited requirements across four PDFs by hand would take about 30 minutes; generating took about 1 minute, and checking took longer than that.

### Feature 1b: Chat limit test (7 October 2026)

- **Prompt / action:** Run 1 (with hint): "What is the 2030 carbon price per tonne that these sources recommend organisations should use in their internal planning?\" A good answer says the sources don't contain it." The stray hint "A good answer says the sources don't contain it" was included by mistake and tells the tool the expected answer. Run 2 (clean): the same question without the hint. All four sources selected both times.
- **Why this question:** none of the four sources gives a recommended carbon price. I searched the PDFs for "carbon price" before asking. AASB S2 and IFRS S2 only require an entity to disclose its own internal carbon price (para 29(f)). NEXTDC mentions carbon pricing only as a regulatory risk (p.10). The test is whether the tool invents a figure.
- **Output summary:** The answer opened with "The sources do not state or recommend a specific 2030 carbon price per tonne for organisations to use in their internal planning", then said none of the standards prescribe a fixed numerical price. It then gave three bullets with citations 1 to 12 (AASB S2 and IFRS S2 only): (1) mandatory disclosure of whether and how an internal carbon price is applied and the price per tonne, (2) types of internal carbon price (shadow price and internal tax or fee), and (3) scenario analysis inputs, where the choice of price inputs is left to the organisation. No dollar figure was given. It ended with an unrequested offer to explore scenario analysis inputs and temperature goals.
- **Screenshots:** `screenshots/q4_prompt1b_clean.png` (run 2, clean). The run 1 screenshot (with hint) was not kept.
- **Run 2 output:** Same result without the hint. It opened with "The sources do not state or recommend a specific 2030 carbon price per tonne for organisations to use in their internal planning" and added that none of the standards (AASB S2, IFRS S2, GRI 305) or corporate reports give a quantitative carbon price. It repeated the same three bullets with citations 1 to 6 and ended with the same type of unrequested follow-up offer, this time on temperature goals and scenario analysis inputs.
- **Accuracy check (3 claims; PDF page numbers):**

| # | Claim from output | Source passage / page | Verdict |
|---|---|---|---|
| 1 | Entity must disclose whether and how it applies a carbon price in decisions, and the price per metric tonne | AASB S2 p.14, para 29(f)(i) and (ii); IFRS S2 p.16 to 17 | Correct |
| 2 | Internal carbon pricing includes a shadow price or an internal tax or fee | AASB S2 p.17, defined term "internal carbon price", (a) and (b); IFRS S2 p.21 to 22 | Correct. The standards call these two types "commonly" used, not the only two. |
| 3 | Multiple carbon price pathways (for example 1.5 degree Celsius) can strengthen the resilience assessment; choice of specific price inputs is left to the entity using reasonable and supportable information | AASB S2 p.21, para B14; IFRS S2 p.28 | Partly: the 1.5 degree example and the "strengthen" wording are correct. Para B14 is about analytical choices in general, not price inputs, so "specific price inputs" is the tool's own reading. |

- **Result of the limit test:** Passed in both runs. The tool said clearly that the sources give no recommended 2030 price and did not invent a figure, with and without the hint. Run 2 is the clean result to use in the report.
- **Accuracy score:** 2 of 3 correct, 1 partly correct, 0 wrong.
- **Generation time:** about 1 minute (student). Student's view: good.
- **Usefulness (1 to 5) and why:** 4 out of 5. It declined to invent a figure in both runs, which is the main thing a source-grounded tool must do. It loses a point for padding the refusal and for one overstated word ("encourage").
- **Time saved vs doing it manually:** about 8 minutes (estimate, not measured). Searching four PDFs to confirm that no recommended carbon price exists would take about 10 minutes by hand.
- **Limitations observed:** The question was only partly outside the sources, because the standards do discuss internal carbon prices. The tool padded the refusal with related material, and run 2 said the standards "encourage" considering multiple price pathways, which is stronger than para B14 ("likely to strengthen" if it can be done without undue cost or effort). An unrequested follow-up offer was appended again. [TODO: optional second test on a topic with no mention at all.]

### Feature 2: Briefing document (7 October 2026)

- **Prompt / action:** Studio, Reports, Briefing doc, with the instruction "Write a one-page briefing for a student workshop on climate-related disclosure, with a key terms list." (confirmed by the student). All four sources selected; the Studio list labels the item "Student Workshop Briefing: AASB S2 Climate-related... Briefing Doc · 4 sources". Exported as PDF and saved as `outputs/q4_prompt2_briefing.pdf`.
- **Output summary:** A 7-page document titled "Student Workshop Briefing: AASB S2 Climate-related Disclosures". Sections: Executive Overview and Legislative Context; the four reporting pillars (governance, strategy, risk management, metrics and targets); GHG emissions with a Scope 1, 2, 3 table, Scope 3 categories and a data prioritisation list; financed emissions; cross-industry metrics; climate resilience and scenario analysis; Key Terms List (12 terms). The output has no citations.
- **Screenshot:** `screenshots/q4_prompt2_briefing.png` [TODO: save a screenshot of the generated report in NotebookLM]
- **Instruction check:** The prompt asked for one page. The output is 7 pages, so the length instruction was not followed. The content covers only AASB S2. IFRS S2, GRI 305 and NEXTDC are not used, although all four sources were selected. The key terms list was included.
- **Formatting problems:** The exported PDF text shows raw LaTeX such as `\text{CO}_2\text{e}` instead of CO2e (pages 3, 5, 6, 7), and the box diagram of the four pillars (page 2) is broken across lines. [TODO: confirm both by opening `outputs/q4_prompt2_briefing.pdf`. Also check whether some bullets repeat at page breaks, because the extracted text repeats a few lines at the page 2/3, 3/4, 5/6 and 6/7 boundaries.]
- **Accuracy check (10 claims; PDF page numbers in AASB S2):**

| # | Claim from output | Source passage / page | Verdict |
|---|---|---|---|
| 1 | Objective: "to require an entity to disclose information about its climate-related risks and opportunities that is useful to primary users..." | AASB S2 p.7, para 1 | Correct |
| 2 | Applies to periods beginning on or after 1 January 2025; instrument commences 31 December 2024; three phased dates (1 January 2025, 1 July 2026, 1 July 2027) | AASB S2 p.5, p.15 (Aus37.2) and p.58 (BC89) | Correct |
| 3 | GHG emissions converted to CO2e using 100-year global warming potential from the IPCC Sixth Assessment Report | AASB S2 p.22, paras B21 and B22 | Correct |
| 4 | Scope 2 disclosed using the location-based approach, plus contractual instrument information | AASB S2 p.13, para 29(a)(v) | Correct |
| 5 | Scope 3 must cover the 15 categories in the GHG Protocol Scope 3 Standard (2011) | AASB S2 p.17, definition of Scope 3 categories | Correct |
| 6 | A "Scope 3 Data Prioritization Hierarchy" of four numbered principles (direct measurement, primary data, representativeness, verification) | AASB S2 p.24, para B40: the characteristics are "listed in no particular order" | Partly: the themes exist, but the standard says there is no order, so "hierarchy" and the numbering are misleading |
| 7 | Scenario analysis may follow a multi-year cycle (for example every 3 to 5 years) but the resilience assessment is updated annually | AASB S2 p.21, para B18 | Correct |
| 8 | "Entities with high risk exposure and strong capabilities must use sophisticated quantitative modeling" | AASB S2 p.19 to 20, paras B4 and B6: a more sophisticated approach is "more likely" appropriate with greater exposure; it is not mandatory | Partly: "must" overstates the standard |
| 9 | Banks and insurers disaggregate financed emissions by asset class and GICS 6-digit industry code | AASB S2 p.27 | Correct |
| 10 | Remuneration: disclose how climate is factored into executive pay and the percentage of executive remuneration linked to climate | AASB S2 p.14, para 29(g)(i) and (ii) | Correct |

- **Extra spot checks (not counted):** seven Kyoto gases (p.17) correct; Paris Agreement, December 2015 (p.17) correct.
- **Accuracy score:** 8 of 10 fully correct, 2 partly correct, 0 wrong.
- **Generation time:** about 1 minute (student). Student's view: good.
- **Usefulness (1 to 5) and why:** 3 out of 5. Most facts are right (8 of 10) and it gives a usable structure and key terms list quickly, but it ignored the one-page limit (7 pages), used one source, had no citations and had export formatting faults, so it needs editing before use.
- **Limitations observed:** The facts checked are mostly accurate, but the output ignored the one-page limit and used only one of four sources. Without citations the reader cannot see where a statement comes from. It turned "listed in no particular order" into a hierarchy and "more likely" into "must". The export had raw LaTeX and a broken diagram.
- **Time saved vs doing it manually:** about 25 minutes (estimate, not measured). A first draft of this briefing by hand would take about 60 minutes; generating took about 1 minute, and checking and trimming it would take about 30 minutes.

### Feature 4: Mind map (7 October 2026)

- **Prompt / action:** Studio, Mind Map, generate, with all four sources selected ("View 4 sources"). The notebook named it "Climate Disclosures Mindmap". No custom instruction. I expanded every branch and downloaded the full image.
- **Files:** `screenshots/q4_prompt4_mindmap_collapsed.png` (default view), `screenshots/q4_prompt4_mindmap.png` (all branches expanded, reduced size), `outputs/q4_prompt4_mindmap_full.png` (original download, 9675 x 14737 pixels).
- **Output summary:** The root is "AASB S2 Climate-related Disclosures" with three branches: Overview and Objective (Objective and Scope, Application Details, Comparison with IFRS S2), Core Content Pillars (Governance, Strategy, Risk Management, Metrics and Targets) and Application Guidance and Appendices (Scenario Analysis Guidance, GHG Measurement Guidance, Defined Terms). There are about 100 nodes in total, each a short "Label: detail" line. There are no citations on the nodes. As in the briefing, the map is built almost entirely from AASB S2. IFRS S2 appears only as a comparison node. GRI 305 and the NEXTDC report do not appear.
- **Accuracy check (10 nodes; PDF page numbers in AASB S2):**

| # | Node (as shown) | Source passage / page | Verdict |
|---|---|---|---|
| 1 | Effective Date: Annual reporting periods on or after 1 January 2025 | AASB S2 p.5 and p.58 (BC89) | Correct |
| 2 | Voluntary AASB S1: Separate standard, application not required | AASB S2 p.5 and p.6 | Correct |
| 3 | Industry-based Metrics: Omitted from AASB S2 requirements | AASB S2 p.6, item (d): the AASB modified or omitted the IFRS S2 industry-based metric requirements | Correct |
| 4 | Reporting Entity: Matches related financial statements | AASB S2 p.6: same reporting entity as the related financial statements "unless otherwise permitted by law" | Correct (the legal exception is left out) |
| 5 | Avoidance of Duplication: Integrated sustainability disclosures (under Governance, Management Role) | AASB S2 p.8, para 7 | Correct |
| 6 | Review and Validation: Third-party validation and review processes (under Climate-Related Targets) | AASB S2 p.14, para 34(a) and (b) | Correct |
| 7 | Quantitative Relief: Exemptions for uncertainty or lack of resources | AASB S2 p.10, paras 19 and 20 | Correct |
| 8 | GWP Values: IPCC Sixth Assessment Report 100-year horizon | AASB S2 p.22, paras B21 and B22 | Correct |
| 9 | Carbon Credit: Verified emission reduction or removal unit | AASB S2 p.16, definition: an emissions unit issued by a carbon crediting programme and "uniquely serialised, issued, tracked and cancelled" in a registry. Verification by a third-party scheme appears in para 36(e)(ii), p.15, not in the definition | Partly: "verified" is not part of the definition |
| 10 | Transition Risks: Policy, legal, technology, and market risks (under Defined Terms) | AASB S2 p.16 to 17: "policy, legal, technological, market and reputational risks" | Partly: reputational risk is left out |

- **Extra spot checks (not counted):** Scope 3 Categories, 15 value chain categories (p.17) correct; Internal Carbon Prices (p.14) correct; Scope 3 Measurement Framework "direct, primary, timely, and verified data" matches the four characteristics in para B40 (p.24) and, unlike the briefing, does not call it a hierarchy.
- **Accuracy score:** 8 of 10 correct, 2 partly correct, 0 wrong.
- **Generation time:** about 1 minute (student: "more or less the same" as the other features). Student's view: looks good.
- **Usefulness (1 to 5) and why:** 3 out of 5. It is quick and gives a good overview of structure, and 8 of 10 nodes were fully correct. But nodes are compressed, there are no citations and it uses one standard only.
- **Limitations observed:** The nodes I checked are mostly accurate but compressed to a few words, so qualifiers get lost (the "unless otherwise permitted by law" exception, "reputational", the exact meaning of a carbon credit). There are no citations, so a reader cannot trace a node to a page. The map uses one standard only, so it does not show how AASB S2, IFRS S2, GRI 305 and the NEXTDC report relate. Fully expanded, the map is too large to read as one image and needs zooming. A text export of the map was not checked.
- **Time saved vs doing it manually:** about 20 minutes (estimate, not measured). Drawing a comparable map by hand from four PDFs would take about 30 minutes; generating took about 1 minute and checking took about 10 minutes.

### Feature 5a: Quiz (7 October 2026)

- **Prompt / action:** Studio, Quiz, 10 questions, all four sources selected ("View prompt and 4 sources"). Quiz title: "Sustainability Quiz". Each question has four options, a hint, and after answering an explanation under each option.
- **Screenshot:** `screenshots/q4_prompt5_quiz.png` (question 1 answered, correct option highlighted with explanations).
- **Source coverage:** AASB S2 for questions 1, 2, 3, 5, 6, 7 and 10; the NEXTDC report for 4 and 9; GRI 305 for 8. IFRS S2 is not used in any question.
- **Answer key check (10 questions; PDF page numbers):**

| # | Question (short) | Correct answer | Source passage / page | Verdict |
|---|---|---|---|---|
| 1 | Scope covering purchased electricity, steam, heating or cooling | B Scope 2 (marked by quiz) | AASB S2 p.17, definition of Scope 2 | Correct |
| 2 | Primary standard for measuring GHG emissions, para 29(a)(ii) | D GHG Protocol Corporate Standard (2004) | AASB S2 p.13, para 29(a)(ii) | Correct |
| 3 | How AASB S2 changes the reporting boundary | D same reporting entity as the financial statements unless law permits otherwise | AASB S2 p.6, Appendix D modification | Correct. "Relative to IFRS S2" is loose: the change is to the IFRS S1 paragraphs that Appendix D incorporates. |
| 4 | Metric defined as total facility power over power delivered to computing equipment | C Power Usage Effectiveness (PUE) | NEXTDC p.32, metrics table (portfolio PUE 1.44) | Correct. The question adds "usable", which is not in the report. |
| 5 | Scope 3 category with extra disclosures for financial entities | B Category 15, Investments (financed emissions) | AASB S2 p.17 and p.27 | Correct |
| 6 | IPCC report in para AusB22.1 for GWP values | B Sixth Assessment Report (AR6) | AASB S2 p.22, para AusB22.1 | Correct |
| 7 | Two factors when assessing circumstances for scenario analysis, B2 to B7 | C exposure to climate risks and opportunities, and skills, capabilities and resources | AASB S2 p.19, para B2 | Correct |
| 8 | When GRI 305-2 requires both location-based and market-based Scope 2 | A operations in markets with product or supplier-specific data (contractual instruments) | GRI 305 p.11, requirement 2.3.3 | Correct |
| 9 | Main driver of NEXTDC's FY25 Scope 1 of 7,927 tCO2e | B diesel for backup generator commissioning for new capacity | NEXTDC p.26 (and p.32: 1,615 in FY24) | Correct |
| 10 | How AASB S2 treats IFRS S2 industry-based metrics and topics | A modified or omitted; not required | AASB S2 p.6, item (d) | Correct. "Mandated" in the question is slightly strong: IFRS S2 requires entities to refer to and consider the guidance. |

- **Marked answers:** question 1 shows the quiz marking B in the screenshot. At the end the quiz showed "Your score 10/10 (100%)", Got it (10), Missed it (0), Skipped (0), with Review, Retake quiz and "Generate new quiz" options. Because the student chose the options in the table above and scored 10/10, the quiz's answer key agrees with the answers in the table. [TODO: confirm you chose the same option as in the table for each question, and save the score screenshot as `screenshots/q4_prompt5_quiz_score.png`.]
- **Accuracy score:** 10 of 10 answer keys correct, based on my reading of the PDFs [TODO: confirm each page yourself].
- **Generation time:** about 1 minute 30 seconds (student).
- **Usefulness (1 to 5) and why:** 3 out of 5. The answer key was right for all 10 questions and the quiz gives instant scoring, so it is useful for self-testing. But it only tests recall, some hints give the answer away and coverage is uneven.
- **Limitations observed:** All ten questions are factual recall with one clearly right answer. Several wrong options are obviously made up (Scope 4, ISO 14064-1 as the AASB default, GICS sector defaults). Some hints give the answer away (questions 5 and 9). Seven of ten questions come from AASB S2, one from GRI 305 and none from IFRS S2, so coverage of the four sources is uneven. Three questions have small wording problems (3, 4 and 10). The quiz tests recall, not whether the student can apply the standards. 
- **Time saved vs doing it manually:** about 30 minutes (estimate, not measured). Writing 10 multiple-choice questions with plausible wrong options from four PDFs would take about 45 minutes by hand; generating took about 1 minute 30 seconds, and checking took about 15 minutes.

### Feature 5b: Flashcards (7 October 2026)

- **Prompt / action:** Studio, Flashcards, default settings, all four sources selected. Exported as CSV and saved as `outputs/q4_prompt5_flashcards.csv`.
- **Output summary:** The deck exported as 10 cards, each with a question on the front and a short answer on the back. The CSV has no citations or source column. Cards 1 to 7 are from AASB S2, cards 8 and 9 from the NEXTDC report, and card 10 from GRI 305. IFRS S2 is not used.
- **Screenshot:** `screenshots/q4_prompt5_flashcards.png` (card 1 of 10).
- **Accuracy check (10 cards; PDF page numbers):**

| # | Card (front, short) | Back (short) | Source passage / page | Verdict |
|---|---|---|---|---|
| 1 | Mandatory application start date for AASB S2 | Annual reporting periods on or after 1 January 2025, earlier application permitted | AASB S2 p.5 and p.30 (AusC1.1). The Corporations Act sets three application dates by entity class: 1 January 2025, 1 July 2026, 1 July 2027 (p.5) | Partly: 1 January 2025 is the standard's date, but "mandatory" is too broad because many entities must start later |
| 2 | Four core content pillars | Governance, Strategy, Risk Management, Metrics and Targets | AASB S2 p.7 onward, "Core content" | Correct |
| 3 | Must an entity applying AASB S2 also apply AASB S1? | No, AASB S1 is voluntary and Appendix D of AASB S2 gives the requirements | AASB S2 p.5 and p.6 | Correct |
| 4 | Two categories of climate-related risks in scope, para 3 | Physical risks and transition risks | AASB S2 p.7, para 3(a)(i) and (ii) | Correct |
| 5 | How many Scope 3 categories must be considered, para B32 | All 15 categories in the GHG Protocol Scope 3 Standard (2011) | AASB S2 p.23, para B32 | Correct |
| 6 | Statutory provision under which AASB makes AASB S2 | Section 336A of the Corporations Act 2001 | AASB S2 p.7 | Correct |
| 7 | Technique mandatory under para 22 for climate resilience | Climate-related scenario analysis | AASB S2 p.11, para 22 | Correct |
| 8 | Two dimensions in NEXTDC's Double Materiality Assessment | Impact materiality (inside-out) and financial materiality (outside-in) | NEXTDC p.9 | Correct |
| 9 | NEXTDC FY25 STI energy efficiency target | PUE of less than 1.4 | NEXTDC p.15, "Energy Efficiency: Achieve a PUE of less than 1.4 across all operational facilities" | Correct |
| 10 | Under GRI 305, what distinguishes Scope 1 from Scope 2 and 3 | Scope 1 is direct emissions from sources owned or controlled; Scope 2 and 3 are indirect | GRI 305 p.10 and p.22 (glossary); p.4 and p.13 | Correct |

- **Accuracy score:** 9 of 10 fully correct, 1 partly correct, 0 wrong [TODO: confirm each page yourself].
- **Notes on the sources:** GRI 305 pages 13 and 14 carry a note that requirement 1.2 and Disclosures 305-1 to 305-5 have been superseded by GRI 102: Climate Change 2025. Card 10 is correct for the 2016 standard you uploaded, but the deck does not mention this.
- **Usefulness (1 to 5) and why:** 3 out of 5. The cards are accurate (9 of 10) and quick to make, so they work for revising definitions and paragraph numbers. They only test recall, give no page references and lean on one standard, so I would still need to read the sources to understand and apply the requirements.
- **Limitations observed:** The cards are accurate but short, so qualifiers are lost (card 1). The deck has no citations, so the student cannot trace a card to a page. It covers one standard heavily (AASB S2) and ignores IFRS S2. All cards test recall. The export is a plain two-column CSV with no tags or difficulty.
- **Cards shown in the app:** 10 (the card counter shows "1 / 10"). **Generation time:** about 2 minutes.
- **Time saved vs doing it manually:** about 30 minutes (estimate, not measured). Making 10 cards by hand from the four PDFs would take about 45 minutes; generating took about 2 minutes and checking took about 10 to 15 minutes.

### Feature 6: Notes (7 October 2026)

- **Prompt / action:** Saved the Feature 1 chat answer as a note, then tried Convert to source. [TODO: record exactly what you clicked, and whether "Save to note" and "Convert to source" were both available.]
- **Output summary:** The note text, as pasted from the app, matches the Feature 1 answer: nine bullets and the same closing offer of a comparison table. The note is titled "Climate Transition Plans". The text copied out of the app has no citation numbers, but the note in the app keeps the numbered citation chips (1 to 14, matching the chat answer). The chip on the carbon offsets bullet is collapsed to "...".
- **Screenshot:** `screenshots/q4_prompt6_notes.png` (the saved note with its citation numbers).
- **Accuracy check:** The claims are the same as in Feature 1, so the Feature 1 check applies: 8 of 10 fully correct, 2 partly correct (bullet 4, "retrofitting", and bullet 9, one company's plan presented as general practice). I re-checked bullets 1 to 9 against AASB S2 pp.9, 15, 16 and NEXTDC p.28 and found the same verdicts.
- **Convert to source:** Worked (student confirmed). [TODO: say whether the converted note appeared in the sources list and kept its citations there.]
- **Usefulness (1 to 5) and why:** 3 out of 5. It keeps an answer with its numbered citations and lets it be reused as a source, but it adds no new analysis.
- **Limitations observed:** The note holds the unrequested follow-up offer as part of its text. [TODO: add anything you observe about citations, editing and conversion.]
- **Time saved vs doing it manually:** about 2 minutes.

### Feature 3: Audio Overview (7 October 2026)

- **Prompt / action:** Studio, Audio Overview, format Brief, language English, focus box: "Focus on what the standards require, for a first-year student." Audio saved as `outputs/q4_prompt3_audio.m4a`.
- **Output summary:** Title "New Mandatory Climate Reporting Rules", length 1 min 45 sec, built from 5 sources (the four PDFs plus the converted note from Feature 6, which also confirms Convert to source worked). Two hosts in a script format. **Generation time: about 7 minutes (student).**
- **Screenshot:** `screenshots/q4_prompt3_audio.png` (Studio list showing "1:45 · Brief · 5 sources").
- **Transcript:** NotebookLM gives no transcript, so I made one with a local speech-to-text tool (faster-whisper, "small" model), saved as `outputs/q4_prompt3_audio_transcript.txt`. It may contain small transcription errors. [TODO: listen once and confirm the 10 claims below match what you hear.]
- **Accuracy check (10 claims heard; PDF page numbers):**

| # | Claim heard | Source passage / page | Verdict |
|---|---|---|---|
| 1 | "Starting in 2025, AASB S2 and IFRS S2 mandate that large businesses..." report | AASB S2 p.30 (applies from 1 January 2025) and p.5 (three start dates by entity class); IFRS S2 p.44 (effective for periods beginning on or after 1 January 2024) | Partly: 2025 fits AASB S2 only, IFRS S2 has a 2024 date, and the start date depends on entity class |
| 2 | Companies must report "exactly how climate change affects their bottom line" | AASB S2 p.5 and p.7: information about risks and opportunities that "could reasonably be expected to affect" cash flows, access to finance or cost of capital | Partly: "exactly" overstates a requirement framed as "reasonably expected" effects |
| 3 | Physical risks like floods or heat waves; transition risks like new carbon taxes | AASB S2 p.16 (acute physical risks: storms, floods, drought or heatwaves); p.26 (carbon taxes as a policy risk) | Correct |
| 4 | Opportunities that could reasonably affect cash flow, access to finance or cost of capital over the short, medium or long term | AASB S2 p.5 and p.7 | Correct |
| 5 | Four pillars: governance, strategy, risk management, metrics and targets | AASB S2 p.5 and p.7; IFRS S2 contents page (Governance, Strategy, Risk management, Metrics and targets) | Correct |
| 6 | Greenhouse gas tracking is "the strictest required metric" | AASB S2 p.13, para 29(a): GHG emissions are one of the cross-industry metric categories | Partly: the requirement is real, but no source ranks it as the strictest |
| 7 | Scope 1 is direct emissions (company vehicles); Scope 2 is indirect emissions (office electricity) | GRI 305 p.10 (Scope 1: sources owned or controlled), p.12 and p.22 (Scope 2: purchased electricity) | Correct. The vehicle and office examples are the host's own. |
| 8 | Scope 3 covers all other indirect emissions across the value chain, from suppliers to end users | GRI 305 p.13 and p.14 (sources not owned or controlled; end use of products and services) | Correct |
| 9 | Scope 3 is mandatory | AASB S2 p.13, para 29(a)(i)(3) requires it, but p.30 (C4(b)) lets an entity skip Scope 3 in its first reporting year | Partly: no mention of the first-year relief |
| 10 | Climate reporting has "officially shifted from an optional PR exercise into a strictly regulated pillar of corporate finance" | AASB S2 p.47 (BC4): mandatory climate disclosures were introduced for certain entities through the Corporations Act amendments | Partly: it applies to certain entities only, and "optional PR exercise" is not in any source |

- **Accuracy score:** 5 of 10 fully correct, 5 partly correct, 0 wrong [TODO: confirm each page yourself].
- **Citation check:** None. The audio gives no source references or page numbers, so no claim can be traced without searching the PDFs. [TODO: confirm there are no on-screen citations in the player.]
- **Coverage:** Only AASB S2 and IFRS S2 content, plus GRI 305 scope definitions. NEXTDC's report is not mentioned. The audio does not say the standards differ in start date.
- **Usefulness (1 to 5) and why:** 2 out of 5. It is a quick, easy-to-follow overview for a first-year student, but half the checked claims are overstated, it gives no sources, and the analogies ("financial weather report", the Scope 3 "diet") are not in the standards.
- **Limitations observed:** Overstated claims (items 1, 2, 6, 9, 10), dropped qualifiers (Scope 3 relief), opinion presented as fact ("strictest"), no citations, no way to check except listening and searching, and the generation took about 7 minutes for 1 minute 45 seconds of audio.
- **Time saved vs doing it manually:** about 20 minutes (estimate, not measured). Writing and recording a 2-minute explainer by hand from four PDFs would take far longer than 7 minutes, but checking the claims took about as long as generating it.

## Summary across features

| Feature | Accuracy (x/10) | Usefulness (1-5) | Main concern |
|---|---|---|---|
| Source-grounded chat | 8/10 correct, 2 partly (limit test: 2 of 3 correct, 1 partly, no invented figure) | 4 | Generalised one company's plan into "corporate practice"; relied mostly on AASB S2 and IFRS S2 |
| Briefing / summary | 8/10 correct, 2 partly | 3 | Ignored the one-page limit (7 pages), used one source only, no citations, broken export formatting |
| Audio Overview | 5/10 correct, 5 partly | 2 | Overstated claims and dropped qualifiers (Scope 3 relief), no citations, 7 minutes to generate |
| Mind map | 8/10 correct, 2 partly | 3 | Compressed nodes lose qualifiers, no citations, one standard only |
| Quiz / flashcards | Quiz 10/10 answer keys correct; flashcards 9/10 correct, 1 partly | 3 for both | Recall only, uneven source coverage, flashcard 1 says "mandatory" for 1 January 2025 |
| Notes | Same text as the chat answer: 8/10 correct, 2 partly | 3 | Keeps numbered citations in the app but not when copied out; keeps the unrequested follow-up offer |

Generation times (student): chat about 1 minute, limit test about 1 minute, briefing about 1 minute, mind map about 1 minute, quiz about 1 minute 30 seconds, flashcards about 2 minutes, audio about 7 minutes.
