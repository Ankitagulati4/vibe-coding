"""
SLIDE 7 · PART 1 · HTTPX — One client, sync or async
-----------------------------------------------------
Every agent eventually calls an external API. httpx gives you the
same, familiar API for both blocking scripts and async agent code.

We use https://httpbin.org — a free request/response echo service —
so the demo actually runs without any API keys.

RUN:  python 03_httpx_sync_async.py
"""

import asyncio

import httpx


def sync_demo() -> None:
    print("SYNC — fine for scripts and simple tools")
    # A plain GET request, blocking until the response arrives.
    response = httpx.get("https://httpbin.org/get", params={"city": "Hyderabad"})
    response.raise_for_status()          # turn HTTP 4xx/5xx into an exception
    data = response.json()
    print("  Status :", response.status_code)
    print("  Echoed :", data["args"])   # httpbin echoes our query params back


async def async_demo() -> None:
    print("ASYNC — what you'll actually use inside an agent")
    async with httpx.AsyncClient() as client:
        # Kick off the request WITHOUT waiting yet — we get back a task.
        task = asyncio.create_task(
            client.post("https://httpbin.org/post", json={"query": "vibe coding"})
        )
        # This line runs immediately, while the request is still in flight —
        # proof that async doesn't sit and wait.
        print("  ...request sent, I'm NOT waiting — running this line meanwhile!")
        response = await task            # NOW wait for the reply to come back
        response.raise_for_status()
        results = response.json()
        print("  Status :", response.status_code)
        print("  Sent   :", results["json"])   # httpbin echoes our JSON body


def main() -> None:
    sync_demo()
    print("-" * 50)
    asyncio.run(async_demo())


if __name__ == "__main__":
    main()
