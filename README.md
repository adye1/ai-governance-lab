# AI Governance & Security Lab

A hands-on lab that pairs **adversarial AI security testing** with **AI governance evidence**, built on self-hosted open-weight models. The goal is to demonstrate — not just describe — what AI risk looks like, whether controls actually reduce it, and how to govern the result, mapped to **NIST AI RMF**, the **OWASP Top 10 for LLM Applications (2025)**, and **MITRE ATLAS**.

> **Why this exists.** Most discussion of AI risk stops at frameworks. This lab closes the loop: attack a live model, measure what got through, apply controls, measure the risk reduction, and produce the governance artifacts a board and an auditor would actually ask for. Everything here runs locally on commodity hardware — no cloud model APIs, no production systems, synthetic data only.

---

## What this lab demonstrates

- **AI red-teaming in practice** — automated adversarial testing of local LLMs against the OWASP LLM Top 10, mapped to MITRE ATLAS techniques.
- **Control effectiveness, measured** — before/after attack-success rates showing whether guardrails actually work, not just that they exist.
- **Governance operationalized** — NIST AI RMF (GOVERN / MAP / MEASURE / MANAGE) turned into concrete evidence: model cards, an AI risk register, an RMF crosswalk, and board-ready metrics.
- **Responsible scope** — a contained, offline environment with a documented safety and ethics model.

## Architecture

Four commodity machines mapped to the four functional pieces of a real AI risk program: the system under test, the attacker, the controls, and the governance/evidence function.

| Node | Role |
|------|------|
| Model host (workstation, 128 GB RAM, GPU) | Runs local open-weight models + the systems under test (a RAG app and an agentic app) |
| Red-team node | Automated adversarial testing (garak, PyRIT, promptfoo) |
| Guardrails node | The control layer — LLM firewall / guardrails / logging |
| Governance node | AI inventory, model cards, RMF crosswalk, risk register, evidence store |

<!-- Replace this comment with an architecture diagram (diagrams/architecture.png). A Mermaid version renders natively on GitHub. -->

## Repository map

| Path | Contents |
|------|----------|
| `docs/` | Design decisions, safety & ethics model, setup notes, methodology |
| `frameworks/` | The NIST AI RMF crosswalk, OWASP LLM Top 10 test map, ISO 42001 mapping |
| `systems-under-test/` | The RAG and agentic apps used as targets (code only — see note below) |
| `red-team/` | OWASP-mapped adversarial test suites and (sanitized) results |
| `controls/` | Guardrail patterns and measured effectiveness |
| `governance/` | AI inventory, model/system cards, risk register, policy templates, metrics |
| `capstone/` | A complete, RMF-structured AI risk assessment (the headline artifact) |

## Frameworks referenced

- **NIST AI RMF 1.0** and the **Generative AI Profile (NIST-AI-600-1)**
- **OWASP Top 10 for LLM Applications (2025)**
- **MITRE ATLAS**
- **ISO/IEC 42001** and the **EU AI Act** (governance breadth)

*Framework versions evolve; where this repo cites specifics, confirm against the source before relying on them.*

## Responsible-use & safety notice

This lab intentionally builds and tests deliberately weak AI applications in order to study detection and defense. It is designed to be run **only against systems the operator owns**, on an **isolated, offline** environment, using **synthetic data**. It contains **no real credentials, no real personal data, and no novel working exploits** — the emphasis is on governance, measurement, and defense. See [`docs/safety-and-ethics.md`](docs/safety-and-ethics.md).

## Security hygiene of this repository

- **No secrets, ever.** A `.gitignore` excludes keys, tokens, environment files, model weights, and the planted-sensitive-data corpus. Secret scanning (**gitleaks**) runs as a pre-commit hook and can be run in CI. Any planted "sensitive" values used for testing are synthetic and kept local, never committed.
- **Clear provenance.** Commits follow a conventional style (`docs:`, `feat:`, `fix:`) and are made incrementally as each phase is built.

## Status

🚧 Actively being built, phase by phase. The commit history reflects the real build sequence.

## License

Released under the [MIT License](LICENSE) — reuse the templates and methods freely.

---

*Maintained as a practitioner's contribution to the AI governance and security community. Feedback and discussion welcome via issues.*
