# Part 1 — Python for Agentic AI

Five tools that show up in almost every agent stack: **Pydantic, httpx, FastAPI, streaming, Streamlit**.

## Setup

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## The demos, in slide order

### Pydantic — give your data a shape (slides 5–6)
```powershell
python 01_pydantic_basics.py
python 02_pydantic_validation.py
```

### httpx — one client, sync or async, streaming (slides 7–8)
```powershell
python 03_httpx_sync_async.py
python 04_httpx_streaming.py
```
> These call the free `httpbin.org` echo service, so they need internet but no API keys.

### FastAPI — a function becomes an API (slides 9–10)
```powershell
uvicorn 05_fastapi_hello:app --reload
# then open http://localhost:8000/health  and  http://localhost:8000/docs

uvicorn 06_fastapi_typed:app --reload
# then open http://localhost:8000/docs and try POST /chat
```

### Streaming through FastAPI (slides 11–12)
```powershell
uvicorn 07_fastapi_streaming:app --reload
# watch words appear live:
curl -N -X POST http://localhost:8000/chat/stream -H "Content-Type: application/json" -d "{\"message\": \"streaming makes agents feel fast\", \"session_id\": \"x\"}"
```

### Streamlit — a UI in minutes (slide 13)
Run the streaming backend AND the UI, in two terminals:
```powershell
# terminal 1
uvicorn 07_fastapi_streaming:app --reload
# terminal 2
streamlit run 08_streamlit_app.py
```

### All five together (slide 14 — architecture)
```powershell
uvicorn 09_full_stack_agent:app --reload
# open http://localhost:8000/docs
# (optional) point 08_streamlit_app.py's BACKEND_URL at this app to drive it from the UI
```

## The mental model (slide 14)

```
STREAMLIT  →  FASTAPI  →  HTTPX  →  LLM provider
  UI           API         call
                 └──────── PYDANTIC shapes data at every hop ────────┘
```
