---id: 1title: Update project constitution with AI/Spec-Driven book principlesstage: constitutiondate: 2025-11-26surface: agentmodel: claude-sonnet-4-5-20250929feature: nonebranch: masteruser: Muhammad Hamid Razacommand: /sp.constitution "Project principles and standards:
- Write a complete AI/Spec-Driven book using Docusaurus and deploy on GitHub Pages
- Build a RAG-based Chatbot embedded in the book using OpenAI Agents SDK, FastAPI, and Qdrant Cloud Free Tier
- Chatbot must answer questions about the book, including user-selected text context
- Create reusable intelligence via Claude Code Subagents and Agent Skills where possible
- Document all agent interactions and AI decisions with error recovery and logging
- Follow production-ready patterns for agent orchestration, API usage, and RAG pipelines
Technical stack:
- Claude Code + Subagents + Agent Skills (primary orchestration layer)
- OpenAI Agent SDK
- FastAPI backend for serving RAG chatbot
- Qdrant Cloud Free Tier for vector database storage and retrieval
- Docusaurus 3.x for book generation and GitHub Pages deployment
- Node.js + Python environment for automation and RAG pipelines
- Local or cloud storage with validation for book and chatbot assets
Quality requirements:
- Generated book must be complete, deployable, and correctly structured on GitHub Pages
- Chatbot must answer queries accurately from entire book and from user-selected context
- Reusable intelligence (skills/subagents) should be modular, testable, and callable on-demand
- All agent operations must include retry logic (max 3 retries) before failing
- Error handling and logging must cover all AI decisions, API calls, and vector searches
- System must be testable end-to-end before submission"
labels: ["constitution", "project-setup"]links:
  spec: null
  ticket: null
  adr: null
  pr: nullfiles:
  - .specify/memory/constitution.mdtests:null---## Prompt"Project principles and standards:
- Write a complete AI/Spec-Driven book using Docusaurus and deploy on GitHub Pages
- Build a RAG-based Chatbot embedded in the book using OpenAI Agents SDK, FastAPI, and Qdrant Cloud Free Tier
- Chatbot must answer questions about the book, including user-selected text context
- Create reusable intelligence via Claude Code Subagents and Agent Skills where possible
- Document all agent interactions and AI decisions with error recovery and logging
- Follow production-ready patterns for agent orchestration, API usage, and RAG pipelines
Technical stack:
- Claude Code + Subagents + Agent Skills (primary orchestration layer)
- OpenAI Agent SDK
- FastAPI backend for serving RAG chatbot
- Qdrant Cloud Free Tier for vector database storage and retrieval
- Docusaurus 3.x for book generation and GitHub Pages deployment
- Node.js + Python environment for automation and RAG pipelines
- Local or cloud storage with validation for book and chatbot assets
Quality requirements:
- Generated book must be complete, deployable, and correctly structured on GitHub Pages
- Chatbot must answer queries accurately from entire book and from user-selected context
- Reusable intelligence (skills/subagents) should be modular, testable, and callable on-demand
- All agent operations must include retry logic (max 3 retries) before failing
- Error handling and logging must cover all AI decisions, API calls, and vector searches
- System must be testable end-to-end before submission"## Response snapshotThe project constitution has been updated to version 1.0.0. The following templates require manual review and update to align with the new principles and sections:
- .specify/templates/plan-template.md
- .specify/templates/spec-template.md
- .specify/templates/tasks-template.md
- .specify/templates/commands/*.md## Outcome- ✅ Impact: Constitution updated with new principles and sections for AI/Spec-Driven book and RAG Chatbot.
- 🧪 Tests: N/A
- 📁 Files: Updated .specify/memory/constitution.md
- 🔁 Next prompts: Address pending template updates.
- 🧠 Reflection: Successfully updated project constitution. Key templates (.specify/templates/*.md) require manual review and update to align with new principles and sections.## Evaluation notes (flywheel)- Failure modes observed: None
- Graders run and results (PASS/FAIL): None
- Prompt variant (if applicable): None
- Next experiment (smallest change to try): None