"""
SLIDE 13 · PART 1 · STREAMLIT — A UI in minutes, no frontend framework
----------------------------------------------------------------------
Streamlit turns a plain Python script into a web app — no HTML, CSS, or
JavaScript needed. Here it's a tiny chat box that sends your message to
the streaming FastAPI backend (07_fastapi_streaming.py) and shows the
reply as it streams in, word by word.

RUN (two terminals):
  1) python -m uvicorn 07_fastapi_streaming:app --reload
  2) streamlit run 08_streamlit_app.py

If the backend isn't running, it falls back to a local echo so the UI
still works.
"""
#python -m uvicorn 07_fastapi_streaming:app --reload
#streamlit run 08_streamlit_app.py

import httpx
import streamlit as st

# The address of our streaming FastAPI backend (from step 07).
BACKEND_URL = "http://localhost:8000/chat/stream"

# st.title draws a big heading at the top of the web page.
st.title("Agent Chat")

def stream_reply(prompt: str):
    """Ask the backend and yield the reply piece by piece as it arrives."""
    # The JSON body our FastAPI /chat/stream endpoint expects.
    payload = {"message": prompt, "session_id": "streamlit-demo"}
    # httpx.stream keeps the connection open so we receive the reply in
    # pieces (a stream) instead of waiting for the whole thing.
    with httpx.stream("POST", BACKEND_URL, json=payload, timeout=30) as resp:
        resp.raise_for_status()          # stop if the backend returned an error
        # iter_text() hands us each chunk as it lands; `yield` passes it
        # straight on to Streamlit to display immediately.
        for chunk in resp.iter_text():
            yield chunk


# st.chat_input draws a chat box at the bottom. When the user types and
# hits Enter, `prompt` holds their text and the code below runs.
# (Streamlit re-runs this whole script top-to-bottom on every message.)
if prompt := st.chat_input("Ask something..."):
    # Show what the user typed, styled as a user chat bubble.
    st.chat_message("user").write(prompt)

    # Everything inside this `with` block appears in an assistant bubble.
    with st.chat_message("assistant"):
        try:
            # st.write_stream consumes our generator and renders each chunk
            # the moment it arrives — so the reply types itself out live.
            st.write_stream(stream_reply(prompt))
        except Exception:
            # Backend not running? Show a simple echo so the demo still works.
            st.write(f"(offline echo) {prompt}")


