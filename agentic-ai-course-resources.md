# Resources for Designing an Undergraduate Course on Agentic AI

A practical starter pack for colleagues building a course on **LLM-based agents**: systems that plan, use tools, remember context, evaluate their own work, and act under human oversight—not chatbots with extra marketing.

This page is intentionally public and self-contained. Use it as a syllabus sketch, a reading list, or a shared bookmark set for a teaching team.

**Suggested audience:** upper-division undergraduates in computer science, information systems, or related majors (or mixed cohorts with strong Python comfort).  
**Suggested length:** one semester (about 14 instructional weeks).  
**Core idea students should leave with:** *an agent is a loop* (model → tools → observation → exit condition), wrapped in specs, evals, and guardrails—not a single clever prompt.

---

## How to use this page

| If you need… | Start here |
|--------------|------------|
| A semester skeleton | [Suggested week-by-week outline](#suggested-week-by-week-outline) |
| Free “textbooks” from labs | [Official guides and open courses](#official-guides-and-open-courses) |
| A dense paper map (hundreds of refs) | [Large paper lists and Chinese open curricula](#large-paper-lists-and-chinese-open-curricula) |
| A short required-reading set | [Core papers](#core-papers-required-set) |
| Lab stack choices | [Recommended tooling stack](#recommended-tooling-stack) |
| Assignment design | [Projects and assessment](#projects-and-assessment) |
| Peer syllabi to borrow structure from | [Existing university courses](#existing-university-courses) |

**Teaching rule of thumb:** assign *one* paper and *one* lab doc per week. Point students at the big paper lists as maps, not as homework.

---

## Learning outcomes (draft)

By the end of a course built on these materials, students should be able to:

1. Distinguish agents from chatbots and from fixed automation workflows.
2. Implement a single-agent tool-using loop with a clear stop condition.
3. Add retrieval (RAG) and simple memory without treating long context as a silver bullet.
4. Design a small evaluation suite (golden cases + a few adversarial prompts) before “improving” the agent with more models or more agents.
5. Apply basic safety patterns: least-privilege tools, human approval for high-impact actions, logging, and ownership when the agent fails.
6. Ship a small but real agent (repository + evals + short demo), and explain its failure modes.

---

## Existing university courses

Useful as structural templates (topics, grading, project banks)—not as materials to copy wholesale.

| Course | Why look at it |
|--------|----------------|
| [UVA CS 6501 — Workshop on Building AI Agents](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/agenticAI.html) (Henry Kautz, Spring 2026) | Hands-on workshop model: mandatory labs, portfolio review, strong project idea list, stack spanning smolagents / LangGraph / MCP / ReAct / RAG / multi-agent. |
| [NYU Stern — Foundations of AI Agents](https://pages.stern.nyu.edu/~ilobel/Foundations_of_AI_Agents.pdf) (Jagabathula & Lobel, Spring 2026) | Compact, business-friendly intensive: chatbot → tools → architecture → multi-agent → eval/RAG → deploy → demo day. Good for non-CS-heavy cohorts. |

---

## Official guides and open courses

These are the cleanest free primary sources. Prefer them over secondary “thread summaries.”

### OpenAI

- [A practical guide to building agents (PDF)](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf) — ~34 pages. Core teaching frame: **the agent is the loop**; start with one agent and more tools before multi-agent.
- OpenAI Agents SDK / cookbook examples (pair with the guide when students implement).

### Anthropic

- [Anthropic Academy](https://anthropic.skilljar.com/) — free courses and certificates.
- [Claude Code 101](https://anthropic.skilljar.com/claude-code-101) — agentic coding harness literacy.
- [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — long-horizon context as a scarce resource.
- Claude docs on prompt engineering and building with tools (assign the official pages, not screenshots of “leaked” prompts).

### Hugging Face and DeepLearning.AI

- [Hugging Face Agents Course](https://huggingface.co/learn/agents-course) — includes **smolagents**, LangChain, and LlamaIndex tracks.
- [MCP Course](https://huggingface.co/learn/mcp-course/en/unit0/introduction) — Model Context Protocol for portable tools.
- [Context Course](https://huggingface.co/learn/context-course/unit0/introduction) — context engineering for coding agents.
- [Building Code Agents with Hugging Face smolagents](https://www.deeplearning.ai/courses/building-code-agents-with-hugging-face-smolagents) (DeepLearning.AI short course).

### Protocols and frameworks (docs, not textbooks)

- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Hugging Face smolagents](https://huggingface.co/docs/smolagents/index)
- [LangChain / LangGraph](https://www.langchain.com) — especially agent architecture writeups
- Optional later: AutoGen, CrewAI, Google ADK — introduce *after* students can write a raw tool loop

---

## Large paper lists and Chinese open curricula

These are especially useful when a colleague asks “where is the field map?”

### Master paper list (hundreds of agent papers)

| Resource | Link | Notes |
|----------|------|--------|
| **WooooDyy / LLM-Agent-Paper-List** | [github.com/WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) | Maintained companion to the Fudan survey below. Organized by brain / perception / action, memory, planning, tools, multi-agent, society, benchmarks. Best single bookmark for “give me the literature tree.” |
| **Survey paper** | [arXiv:2309.07864](https://arxiv.org/abs/2309.07864) — *The Rise and Potential of Large Language Model Based Agents* (Xi et al.) | 86-page SCIS cover survey. Optional whole-course reference architecture; do **not** assign end-to-end to undergrads. |
| **AgentGym** (same lab ecosystem) | [github.com/WooooDyy/AgentGym](https://github.com/WooooDyy/AgentGym) | Environments and trajectories for agent development / RL-style training (advanced or grad track). |

### Full open courses from Datawhale (Chinese open-source education community)

| Resource | Link | Notes |
|----------|------|--------|
| **Hello-Agents** | [github.com/datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents) | *Building Agents from Scratch* — systematic free textbook (Chinese + English). Classic paradigms → low-code tools → frameworks → build-your-own → memory, context engineering, protocols, evals, capstones. Online reading: [datawhalechina.github.io/hello-agents](https://datawhalechina.github.io/hello-agents/) |
| **Agent Learning Hub** | [github.com/datawhalechina/Agent-Learning-Hub](https://github.com/datawhalechina/Agent-Learning-Hub) | Learning roadmap and curated starter papers. |
| Datawhale org | [github.com/datawhalechina](https://github.com/datawhalechina) | Broader open AI education materials. |

### Other focused lists

| List | Link | Focus |
|------|------|--------|
| AGI-Edgerunners / LLM-Agents-Papers | [github.com/AGI-Edgerunners/LLM-Agents-Papers](https://github.com/AGI-Edgerunners/LLM-Agents-Papers) | Ongoing agent paper collection |
| OSU-NLP GUI Agents Paper List | [github.com/OSU-NLP-Group/GUI-Agents-Paper-List](https://github.com/OSU-NLP-Group/GUI-Agents-Paper-List) | Browser / computer-use agents |
| Agent Memory Paper List | [github.com/Shichun-Liu/Agent-Memory-Paper-List](https://github.com/Shichun-Liu/Agent-Memory-Paper-List) | Memory mechanisms |
| RUCAIBox LLMSurvey | [github.com/RUCAIBox/LLMSurvey](https://github.com/RUCAIBox/LLMSurvey) | Broader LLM survey tree |

**Classroom practice:** pin a commit of the paper list at the start of term so links do not move under students mid-semester.

---

## Core papers (required set)

A tight set that covers the mechanics undergrads actually need. Pair each with a lab.

| Topic | Paper | Link |
|-------|--------|------|
| Reason + act loop | **ReAct** — Yao et al., 2022 | [arXiv:2210.03629](https://arxiv.org/abs/2210.03629) |
| Self-improvement via language feedback | **Reflexion** — Shinn et al., 2023 | [arXiv:2303.11366](https://arxiv.org/abs/2303.11366) |
| Multi-agent simulation / memory–reflect–plan | **Generative Agents** — Park et al., 2023 | [arXiv:2304.03442](https://arxiv.org/abs/2304.03442) |
| Hierarchical memory | **MemGPT** — Packer et al., 2023 | [arXiv:2310.08560](https://arxiv.org/abs/2310.08560) |
| Retrieval grounding | **RAG** — Lewis et al., 2020 | [arXiv:2005.11401](https://arxiv.org/abs/2005.11401) |
| Long-context failure modes | **Lost in the Middle** — Liu et al., 2023 | [arXiv:2307.03172](https://arxiv.org/abs/2307.03172) |
| Instruction following / alignment basics | **InstructGPT / RLHF** — Ouyang et al., 2022 | [arXiv:2203.02155](https://arxiv.org/abs/2203.02155) |

### Strong electives (pick by week theme)

| Topic | Starting point |
|-------|----------------|
| Tool learning | Toolformer — [arXiv:2302.04761](https://arxiv.org/abs/2302.04761) |
| Chain-of-thought | Wei et al. — [arXiv:2201.11903](https://arxiv.org/abs/2201.11903) |
| Self-refine | Madaan et al. — [arXiv:2303.17651](https://arxiv.org/abs/2303.17651) |
| Tree of thoughts | Yao et al. — [arXiv:2305.10601](https://arxiv.org/abs/2305.10601) |
| Parameter-efficient tuning | LoRA — [arXiv:2106.09685](https://arxiv.org/abs/2106.09685) |
| Preference optimization | DPO — [arXiv:2305.18290](https://arxiv.org/abs/2305.18290) |
| Multi-agent systems (industry) | Magentic-One — [arXiv:2411.04468](https://arxiv.org/abs/2411.04468) |
| Agent architecture survey | Masterman et al. — [arXiv:2404.11584](https://arxiv.org/abs/2404.11584) |
| Small models for agents | Belcak et al. — [arXiv:2506.02153](https://arxiv.org/abs/2506.02153) |
| Definitions / taxonomy | *AI Agents vs Agentic AI* — [arXiv:2505.10468](https://arxiv.org/abs/2505.10468) |

### Socio-technical readings (for IS / governance-flavored weeks)

Useful when the course is not pure systems engineering:

- Rahwan et al., *Machine Behaviour* (2019)
- Murray & Rhymer, conjoined agency / humans and technology (2020)
- Kellogg, Valentine & Christin, *Algorithms at Work* (2020)
- Berente et al., Managing AI (MISQ special issue introduction, 2021)
- Recent human–AI teaming and trustworthy collaboration surveys (2023–2025)

---

## Recommended tooling stack

Keep the first half of the course framework-light.

| Layer | Suggested default | Notes |
|-------|-------------------|--------|
| Language | Python 3.11+ | — |
| First agent API | One commercial API *or* a small open model on Colab | Prefer cheap models for loops/evals |
| First framework | **smolagents** | Easy to inspect; good HF course support |
| Second framework | Hand-rolled tool loop **or** LangGraph | Teach the loop before the product surface |
| Tools | Function tools → **MCP** | Portable tool I/O |
| Evals | pytest + golden cases; Promptfoo / Inspect AI / LangSmith optional | Make evals mandatory for the final project |
| Coding agents | Claude Code / Copilot / Gemini Code Assist (student tiers) | Teach as *subject matter* in a harness week, not as a substitute for understanding |

**Principle:** one agent + more tools first. Multi-agent only when a single loop’s logic outgrows itself—and only if multi-agent beats a single-agent baseline on the same eval set.

---

## Suggested week-by-week outline

Adjust pacing for CS vs business students; compress Weeks 10–12 for shorter terms.

| Week | Theme | Core resource | Lab product |
|-----:|-------|---------------|-------------|
| 1 | What is an agent? | OpenAI practical guide (first half) | Same task as script vs as a loop |
| 2 | LLM literacy for agents | InstructGPT / RLHF | Spec for success; temperature vs reliability |
| 3 | Tool use & ReAct | ReAct paper + smolagents unit | Agent with ≥3 tools and a stop condition |
| 4 | Planning & reflection | Reflexion (+ optional Self-Refine / ToT) | Retry loop measured on a fixed eval set |
| 5 | RAG & grounding | RAG + Lost in the Middle | Doc Q&A agent with distractor tests |
| 6 | Memory | MemGPT (+ one memory survey) | Summarization vs archival retrieval |
| 7 | Context engineering & MCP | Anthropic context eng + HF MCP course | MCP-connected tools; log token budget |
| 8 | Evaluation | OpenAI guide (guardrails/eval half) | ≥50-case suite + a few adversarial prompts |
| 9 | Multi-agent | Generative Agents (+ Magentic-One skim) | 2–3 specialists; must beat single-agent baseline |
| 10 | Agentic coding harnesses | Claude Code 101 / harness under-the-hood material | Sandboxed mini coding agent |
| 11 | Safety & permissions | Lab security docs + human–agent readings | Red-team; human approval for high-impact tools |
| 12 | Deploying in organizations | Socio-technical readings | Cost, logging, rollback, owner-of-record checklist |
| 13 | Capstone studio | Project bank (UVA / Datawhale / local) | Feature-complete agent + green evals |
| 14 | Demo day | — | 5-minute video + live Q&A + short report |

### Capstone constraints that work well

Require:

- tools + explicit exit condition  
- an evaluation harness with a committed golden set  
- least-privilege tool access  
- a human escalation path for high-impact actions  
- a short failure analysis (not only a happy-path demo)

Prefer single-agent + tools over multi-agent theater unless students can show a measured gain.

---

## Projects and assessment

### Lightweight grading pattern

| Component | Weight (example) |
|-----------|------------------|
| Weekly labs / GitHub portfolio | 25% |
| Short reading memos | 10% |
| Midterm portfolio review | 15% |
| Final project (build + evals + video + report) | 40% |
| Discussion / participation | 10% |

### Project prompts that scale for undergrads

- Campus / course-policy RAG agent with citations  
- Research assistant that retrieves and *must* cite sources  
- Domain tool agent (calendar, grades mock API, library search)  
- Mini coding agent limited to a sandbox repo  
- Multi-agent debate or writer/critic/editor pipeline with scoring  
- MemGPT-style long-session assistant with archival memory  

See also the project banks on the [UVA syllabus](https://www.cs.virginia.edu/~rmw7my/Courses/AgenticAISpring2026/agenticAI.html) and Datawhale Hello-Agents graduation chapters.

### Final rubric (condensed)

| Criterion | Strong | Weak |
|-----------|--------|------|
| Problem framing | Real user and constraints | Thin chat wrapper |
| Architecture | Clear loop, tools, memory choice justified | Framework soup |
| Evals | Golden + adversarial cases; regression story | Demo screenshots only |
| Safety | Least privilege + escalation | Unrestricted shell / send |
| Write-up | Failures and costs discussed | Success path only |
| Reproducibility | README runs end-to-end | “Works on my machine” |

---

## Design notes worth baking into lectures

These show up repeatedly in practitioner discourse and in lab docs; they make good discussion prompts.

1. **Provenance over packaging.** “Deleted lectures” and “$500 course killers” are often repackaged public materials. Teach students to prefer primary PDFs and official docs.
2. **Specification and verification are scarce skills.** Writing what “done” means—and checking it—often matters more than model choice.
3. **Research agents need retrieval and citations.** Multi-persona role-play without grounding multiplies fluency, not coverage.
4. **Prompt-based permissions are not enough.** Authorization should be structural (tool allowlists, environment isolation, human gates), not only wording in a system prompt.
5. **Separate “using coding agents” from “building agents.”** Both belong in a 2026 curriculum; they are different learning outcomes.

---

## One-week prep checklist for a colleague

1. Decide cohort (CS-heavy vs mixed) and lock prereqs (Python + APIs/JSON).  
2. Choose default stack (smolagents + one API + simple eval harness recommended).  
3. Mirror the OpenAI agents PDF and the seven core papers into the LMS.  
4. Bookmark [WooooDyy/LLM-Agent-Paper-List](https://github.com/WooooDyy/LLM-Agent-Paper-List) and [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents); pin commits.  
5. Skim UVA and Stern syllabi for grading/project patterns.  
6. Secure student model access (campus credits, free tiers, or Colab).  
7. Draft Weeks 1–4 labs as a public template repo before term starts.

---

## Related teaching pages

- [Courses and curriculum](courses.md) — university courses I teach or have developed  
- [Selected student projects](student-projects.md) — public student work (when available)  
- [Profile home](README.md)

---

*Curated for colleagues designing undergraduate (or intensive graduate/professional) courses on agentic AI. Links point to public sources; pin versions each term. Suggestions and corrections welcome.*
