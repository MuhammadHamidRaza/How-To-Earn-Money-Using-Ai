# Research Findings: How to Earn Money Using AI Book

## Phase 0: Research & Clarification

### Decision: Python and Node.js Versions
**Rationale**: Choosing stable and actively supported versions ensures long-term maintainability, security, and access to a rich ecosystem of libraries. Python 3.13 offers performance improvements, while Node.js 24 is an LTS release. This balance provides a modern development environment without sacrificing stability.
**Alternatives considered**: Python 3.10, 3.11, 3.12, 3.14 (too new/not LTS); Node.js 20, 22 (older LTS), Node.js 25 (too new, not LTS).

### Decision: Testing Frameworks
**Rationale**: A combination of `pytest` for Python (backend) and `Jest`/`Playwright` for Node.js (frontend) provides comprehensive testing coverage, including unit, integration, and end-to-end testing. These frameworks are industry standards, well-documented, and have strong community support.
**Alternatives considered**: `unittest` for Python; `Vitest`, `Cypress`, `Selenium`, `Puppeteer` for Node.js (each with specific tradeoffs in features or ecosystem integration).

### Decision: Linux Distribution for FastAPI Backend
**Rationale**: Ubuntu 24.04 LTS is a widely adopted, stable, and secure Linux distribution with extensive community support, making it an excellent choice for deploying FastAPI applications in production. Its long-term support ensures consistent updates and a predictable environment.
**Alternatives considered**: Debian 12 (more conservative, potentially older packages), Fedora (faster release cycle, less typical for long-term server deployment), NixOS (declarative, higher learning curve for initial setup), openSUSE.

### Decision: Chatbot Concurrent User Estimate
**Rationale**: A starting estimate of 10-15 concurrent users accounts for the limitations of free-tier services (like Qdrant's LLM token limits being a primary bottleneck, not storage), typical usage patterns for documentation chatbots, and the overhead of a RAG pipeline. This provides a realistic baseline for initial deployment and allows for future scalability planning.
**Alternatives considered**: Higher estimates (unrealistic for free-tier/initial setup), lower estimates (too conservative and may not meet initial user engagement expectations).
