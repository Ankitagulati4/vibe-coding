"""
SLIDE 8 · PART 1 · HTTPX — Streaming a response as it arrives
-------------------------------------------------------------
A "chunk" is one small piece of a bigger reply. Streaming means the
server sends those pieces one at a time, so we can use each the moment
it arrives instead of waiting for the whole thing. This is exactly how
an LLM reply "types itself out" word by word.

This file shows it two ways:
  1. SYNC  — call httpbin.org/stream/5, which sends 5 chunks one at a
             time, and print each chunk as it lands.
  2. ASYNC — build up a sentence word by word, like a live LLM stream.

RUN:  python 04_httpx_streaming.py
"""

import asyncio
import time

import httpx

# /stream/5 tells the server: split your reply into 5 chunks.
URL = "https://httpbin.org/stream/5"


def sync_stream() -> None:
    print("SYNC stream — watch each chunk appear one at a time:")
    # httpx.stream keeps the connection open and feeds us pieces, instead
    # of downloading the whole response before we can touch it.
    with httpx.stream("GET", URL) as response:
        response.raise_for_status()          # stop early if the server errored
        # iter_lines() hands us one chunk at a time; the loop body runs
        # once per chunk, the moment that chunk arrives.
        for i, chunk in enumerate(response.iter_lines(), start=1):
            # flush=True forces it onto the screen immediately (not buffered),
            # and the small sleep lets your eye catch each arrival.
            print(f"  chunk {i} arrived", flush=True)
            time.sleep(0.5)


async def async_stream() -> None:
    print("ASYNC stream — watch a reply build up word by word:")
    print("  ", end="", flush=True)
    # Pretend this sentence is an LLM's answer arriving one word at a time.
    reply = "streaming shows each word the moment it is ready"
    # Each word is printed on the SAME line as soon as it is yielded,
    # so you see the sentence type itself out live.
    async for word in fake_llm_words(reply):
        print(word + " ", end="", flush=True)
    print()   # final newline once the full reply is done


async def fake_llm_words(sentence: str):
    """
    A stand-in for a real LLM stream. Splits the sentence into words and
    `yield`s them one at a time with a small pause — the same producer
    shape a real agent backend uses to relay tokens as they arrive.
    """
    for word in sentence.split():
        await asyncio.sleep(0.3)   # pause between "tokens" so you can see it
        yield word


def main() -> None:
    sync_stream()
    print("-" * 50)
    asyncio.run(async_stream())


if __name__ == "__main__":
    main()
