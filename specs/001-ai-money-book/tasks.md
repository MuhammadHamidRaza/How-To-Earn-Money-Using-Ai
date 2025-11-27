---
description: "Task list for 'How to Earn Money Using AI Book' feature implementation"
---

# Tasks: How to Earn Money Using AI Book

**Input**: Design documents from `specs/001-ai-money-book/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The spec does not explicitly request TDD, but testing is included as part of implementation phases to ensure quality.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/book/`

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create backend project structure in `backend/`
- [x] T002 Initialize Python environment with FastAPI, OpenAI Agent SDK, Qdrant client dependencies in `backend/`
- [x] T003 [P] Configure backend linting and formatting tools in `backend/`
- [x] T004 Create frontend Docusaurus project in `frontend/book/`
- [x] T005 Initialize Node.js environment with Docusaurus dependencies in `frontend/book/`
- [x] T006 [P] Configure frontend linting and formatting tools in `frontend/book/`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T007 Setup Qdrant client connection and collection for book content in `backend/src/services/qdrant_client.py`
- [x] T008 Implement basic FastAPI application `main.py` in `backend/src/api/`
- [x] T009 Configure global error handling and logging for FastAPI in `backend/src/api/main.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Generate AI-Driven Book Content (Priority: P1) 🎯 MVP

**Goal**: Efficiently create high-quality, AI-generated book content.

**Independent Test**: Generate a sample chapter and verify its structure and information.

### Implementation for User Story 1

- [ ] T010 [P] [US1] Create `BookOutline` and `BookContent` models in `backend/src/models/book.py`
- [ ] T011 [US1] Implement `BookOutlineService` for managing book structure in `backend/src/services/book_outline_service.py`
- [ ] T012 [US1] Implement `ContentGenerationService` for AI generation (using OpenAI Agent SDK) in `backend/src/services/content_generation_service.py`
- [ ] T013 [US1] Implement endpoint for outline management and content generation in `backend/src/api/content.py`
- [ ] T014 [US1] Implement logic to store generated content and embeddings in Qdrant via `backend/src/services/qdrant_client.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Embed RAG Chatbot for Interactive Learning (Priority: P1)

**Goal**: Provide an interactive RAG chatbot embedded in the book.

**Independent Test**: Deploy a basic book with the chatbot, ask questions, and verify responses.

### Implementation for User Story 2

- [ ] T015 [P] [US2] Create `ReaderQuery` and `ChatbotResponse` models in `backend/src/models/chatbot.py`
- [ ] T016 [US2] Implement `RAGService` for retrieval and response generation (using OpenAI Agent SDK and Qdrant) in `backend/src/services/rag_service.py`
- [ ] T017 [P] [US2] Create FastAPI endpoint `/chat/query` in `backend/src/api/chatbot.py`
- [ ] T018 [P] [US2] Create FastAPI endpoint `/chat/query-with-context` in `backend/src/api/chatbot.py`
- [ ] T019 [US2] Develop Docusaurus React component for chatbot UI in `frontend/book/src/components/Chatbot.js`
- [ ] T020 [US2] Integrate chatbot UI component into Docusaurus book pages in `frontend/book/src/theme/DocItem/Content/index.js`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Deploy Book on GitHub Pages (Priority: P2)

**Goal**: Publicly accessible AI-generated book on GitHub Pages.

**Independent Test**: Deploy the book and verify accessibility and link functionality.

### Implementation for User Story 3

- [ ] T021 [US3] Configure Docusaurus for GitHub Pages deployment in `frontend/book/docusaurus.config.js`
- [ ] T022 [US3] Setup CI/CD pipeline (e.g., GitHub Actions) for automated Docusaurus build and deployment in `.github/workflows/deploy.yaml`
- [ ] T023 [US3] Verify correct routing and linking in the deployed book via end-to-end tests using `Playwright` in `frontend/book/tests/e2e/deploy_check.spec.js`

**Checkpoint**: All user stories should now be independently functional

---

## Final Phase: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T024 Optimize Docusaurus book content for file size and build time in `frontend/book/`
- [ ] T025 Implement error recovery and retry logic for all agent/API operations in `backend/src/services/`
- [ ] T026 Implement comprehensive logging for all agent decisions, API calls, and queries in `backend/src/`
- [ ] T027 Ensure session persistence for chatbot operations in `backend/src/services/rag_service.py`
- [ ] T028 Enforce rate limiting for Qdrant/API services in `backend/src/api/main.py`
- [ ] T029 Run end-to-end system tests for the entire solution in `tests/e2e/system_test.spec.js`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P1 → P2)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - No dependencies on other stories

### Within Each User Story

- Models before services
- Services before API endpoints / UI components
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- Once Foundational phase completes, User Story 1 and User Story 2 can start in parallel (if team capacity allows, as both are P1)
- Tasks within a story marked [P] can run in parallel

---

## Parallel Example: User Story 1 (Generate AI-Driven Book Content)

```bash
# Launch models for User Story 1 together:
Task: "Create BookOutline and BookContent models in backend/src/models/book.py"

# Or, if services are independent of each other (after models are done):
Task: "Implement BookOutlineService for managing book structure in backend/src/services/book_outline_service.py"
Task: "Implement ContentGenerationService for AI generation (using OpenAI Agent SDK) in backend/src/services/content_generation_service.py"
```

---

## Parallel Example: User Story 2 (Embed RAG Chatbot for Interactive Learning)

```bash
# Launch models for User Story 2 together:
Task: "Create ReaderQuery and ChatbotResponse models in backend/src/models/chatbot.py"

# Launch API endpoints for User Story 2 together:
Task: "Create FastAPI endpoint /chat/query in backend/src/api/chatbot.py"
Task: "Create FastAPI endpoint /chat/query-with-context in backend/src/api/chatbot.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 & 2)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. Complete Phase 4: User Story 2
5. **STOP and VALIDATE**: Test User Story 1 and 2 independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (Partial MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo (Full MVP!)
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1 (P1)
   - Developer B: User Story 2 (P1)
   - Developer C: User Story 3 (P2)
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing (if tests were explicitly requested)
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
