# GitHub Copilot — repo-wide instructions

Conventions Copilot reads automatically for every message in this repo, so you
don't repeat them in every prompt.

## Stack
- Python 3.11+, FastAPI, Pydantic v2, httpx for all outbound calls
- Streamlit for internal UIs and demos

## Code style
- Type-hint every function signature; no bare `Any`
- Validate all API inputs/outputs with Pydantic v2 models
- Use `httpx` (async) for outbound HTTP; never `requests`
- Prefer `async` for anything that does I/O (network, disk)
- Small, single-purpose functions; keep diffs small and reviewable

## Guardrails / Do NOT
- Never hardcode secrets or API keys — read them from environment variables
- Don't commit `.env` files or secrets
- Don't install a new dependency without a clear reason
- New endpoints must validate their input and have at least one test
- Show the diff before applying anything destructive
