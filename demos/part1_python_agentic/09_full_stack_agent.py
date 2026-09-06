"""
SLIDE 14 · PART 1 · ARCHITECTURE — How the five fit together
------------------------------------------------------------
Every agent we build is some version of this chain:

  STREAMLIT  →  FASTAPI  →  HTTPX  →  (LLM provider)
   (UI)         (API)       (call)     └─ PYDANTIC shapes data at every hop

This single backend demonstrates all five working together:
  * PYDANTIC  — ChatRequest / ChatResponse validate every payload
  * FASTAPI   — exposes /chat (typed) and /chat/stream (streaming)
  * HTTPX     — makes the outbound call to an "LLM" (we use httpbin)
  * STREAMING — relays the reply back token-by-token
  * STREAMLIT — point 08_streamlit_app.py's BACKEND_URL here to see it live

RUN:  uvicorn 09_full_stack_agent:app --reload
THEN: open http://localhost:8000/docs
"""

import asyncio

import httpx
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI(title="Full-Stack Agent Backbone")


# ── PYDANTIC: shapes data at every hop ───────────────────────────────
class ChatRequest(BaseModel):
    message: str
    session_id: str


class ChatResponse(BaseModel):
    reply: str
    model: str = "demo-llm"


# ── HTTPX: the outbound call an agent makes to an LLM provider ────────
async def call_llm(message: str) -> str:
    """
    Stand-in for a real LLM call. We POST to httpbin, which echoes our
    payload back — proving the round-trip works without any API key.
    Replace this with a real provider call (OpenAI, Anthropic, etc.).
    """
    async with httpx.AsyncClient() as client:
        resp = await client.post(
            "https://httpbin.org/post",
            json={"prompt": message},
            timeout=30,
        )
        resp.raise_for_status()
        echoed = resp.json()["json"]["prompt"]
    return f"You said: {echoed}"


# ── FASTAPI: the typed, non-streaming endpoint ───────────────────────
@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    reply = await call_llm(req.message)
    return ChatResponse(reply=reply)


# ── STREAMING: the same reply, relayed word by word ──────────────────
@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    reply = await call_llm(req.message)

    async def generate():
        for word in reply.split():
            yield f"{word} "
            await asyncio.sleep(0.15)

    return StreamingResponse(generate(), media_type="text/plain")
