# Session 2 — Demo Code

Runnable demos matching every topic in **`joinloop_session2_python_vibecoding.pptx`**.

Two parts, mirroring the deck:

| Part | Folder | Topics |
|------|--------|--------|
| **Part 1 — Python for Agentic AI** | [`part1_python_agentic/`](part1_python_agentic/) | Pydantic · httpx · FastAPI · Streaming · Streamlit |
| **Part 2 — Vibe Coding, Responsibly** | [`part2_vibe_coding/`](part2_vibe_coding/) | Instructions · Skills · Commands · Hooks |

---

## Quick start

```powershell
# 1. Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 2. Install everything for Part 1
pip install -r part1_python_agentic/requirements.txt
```

Then follow the README in each part folder — every file says how to run it at the top.

## Slide → file map (Part 1)

| Slide | Topic | File |
|-------|-------|------|
| 5  | Pydantic — give data a shape        | `01_pydantic_basics.py` |
| 6  | Pydantic — validation & nested      | `02_pydantic_validation.py` |
| 7  | httpx — sync & async                 | `03_httpx_sync_async.py` |
| 8  | httpx — streaming                    | `04_httpx_streaming.py` |
| 9  | FastAPI — function becomes an API    | `05_fastapi_hello.py` |
| 10 | FastAPI — typed request/response     | `06_fastapi_typed.py` |
| 12 | Streaming back through FastAPI       | `07_fastapi_streaming.py` |
| 13 | Streamlit — a UI in minutes          | `08_streamlit_app.py` |
| 14 | How the five fit together            | `09_full_stack_agent.py` |
