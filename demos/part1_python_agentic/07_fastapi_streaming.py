"""
SLIDE 11 & 12 · PART 1 · STREAMING — Streaming back out through FastAPI
-----------------------------------------------------------------------
Why stream? A visitor who sees nothing for 3-4 seconds assumes it's
broken. Streaming shows the first word almost instantly.

Here we fake an LLM by yielding the request back one word at a time,
with a small delay so you can SEE the streaming in your terminal/browser.
Swap `generate()` for a real `httpx.stream()` LLM call and you have the
backbone of every chat agent.

RUN:  uvicorn 07_fastapi_streaming:app --reload
THEN: curl -N -X POST http://localhost:8000/chat/stream ^
           -H "Content-Type: application/json" ^
           -d "{\"message\": \"streaming makes agents feel fast\", \"session_id\": \"x\"}"
      (the -N flag disables curl buffering so you see words appear live)
"""

import asyncio

from fastapi import FastAPI
# StreamingResponse is FastAPI's way of sending a reply in pieces
# (a stream) instead of all at once.
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

app = FastAPI(title="Streaming FastAPI")


class ChatRequest(BaseModel):
    message: str
    session_id: str


@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    # `generate` is a producer: it yields one piece at a time instead of
    # building the whole reply first. FastAPI sends each yielded piece to
    # the caller the moment it's produced.
    async def generate():
        # Pretend each word is a token arriving from an LLM provider.
        for word in req.message.split():
            yield f"{word} "
            await asyncio.sleep(0.2)   # simulate token-by-token latency

    # Hand the generator to StreamingResponse — FastAPI streams it out.
    # Swap `generate()` for a real httpx.stream() LLM call and this becomes
    # the backbone of a real chat agent.
    return StreamingResponse(generate(), media_type="text/plain")
