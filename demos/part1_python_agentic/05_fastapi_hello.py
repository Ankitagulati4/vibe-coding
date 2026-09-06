"""
SLIDE 9 · PART 1 · FASTAPI — A Python function becomes an API
-------------------------------------------------------------
Decorate a function and you have a live HTTP endpoint. That's it.

RUN:  uvicorn 05_fastapi_hello:app --reload
THEN: open http://localhost:8000/health
      open http://localhost:8000/docs   (auto-generated interactive docs)
"""
#python -m uvicorn 05_fastapi_hello:app --reload

from fastapi import FastAPI

# `app` is the whole web application. uvicorn looks for this exact name
# when you run "uvicorn 05_fastapi_hello:app". `title` just shows up on
# the auto-generated /docs page.
app = FastAPI(title="Hello FastAPI")


# @app.get("/health") is a "decorator" — it attaches the function below
# to a web address. It means: when someone opens the URL "/health" with
# a GET request (what a browser does), run this function and send back
# whatever it returns.
@app.get("/health")
def health():
    # FastAPI turns this Python dict into JSON automatically, so the
    # browser receives: {"status": "ok"}
    return {"status": "ok"}


# You now have a live API on http://localhost:8000
# Try /health in the browser, or explore everything at /docs
