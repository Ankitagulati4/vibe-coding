"""
SLIDE 10 · PART 1 · FASTAPI — Request and response, both typed
--------------------------------------------------------------
Pydantic models describe the request and the response. FastAPI then
validates incoming data for you AND generates interactive docs.

RUN:  uvicorn 06_fastapi_typed:app --reload
THEN: open http://localhost:8000/docs  and try the POST /chat endpoint

Or from another terminal:
  curl -X POST http://localhost:8000/chat ^
       -H "Content-Type: application/json" ^
       -d "{\"message\": \"hello\", \"session_id\": \"abc\"}"
"""
#python -m uvicorn 06_fastapi_typed:app --reload

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Typed FastAPI")


# ChatRequest describes what the CALLER must send us.
# Both fields are required strings — FastAPI rejects anything missing.
class ChatRequest(BaseModel):
    message: str
    session_id: str


# ChatResponse describes what WE send back — just a reply string.
class ChatResponse(BaseModel):
    reply: str


# @app.post("/chat") = handle POST requests (sending data) to /chat.
# response_model=ChatResponse tells FastAPI (and the /docs page) the
# exact shape of the reply.
@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    # Because the parameter is typed as `req: ChatRequest`, FastAPI parses
    # the incoming JSON into a validated ChatRequest before this line runs.
    # req.message is already validated — no manual `if not message` checks.
    # If a client omits a field, FastAPI returns a clean 422 automatically.
    return ChatResponse(reply=f"Echo: {req.message}")


# --- SAMPLES TO TRY on http://localhost:8000/docs (POST /chat) ---
#
# 1) VALID — both fields present, returns {"reply": "Echo: hello"}:
#    {
#      "message": "hello",
#      "session_id": "abc"
#    }
#
# 2) INVALID — session_id missing, returns a 422 validation error:
#    {
#      "message": "hello"
#    }
#
# 3) INVALID — message is a number, not text, returns a 422:
#    {
#      "message": 123,
#      "session_id": "abc"
#    }

