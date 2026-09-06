"""
SLIDE 6 · PART 1 · PYDANTIC — Validation and nested models, for free
--------------------------------------------------------------------
When an LLM returns malformed output, Pydantic gives you a clear,
structured error instead of a mysterious crash three functions later.

RUN:  python 02_pydantic_validation.py
"""

from pydantic import BaseModel, ValidationError


class ToolCall(BaseModel):
    name: str
    arguments: dict


class AgentResponse(BaseModel):
    reply: str
    tool_calls: list[ToolCall] = []   # nested models, validated too


def main() -> None:
    # 1. A well-formed response — including a nested tool call.
    good = AgentResponse(
        reply="Let me check the weather for you.",
        tool_calls=[
            {"name": "get_weather", "arguments": {"city": "Hyderabad"}},
        ],
    )
    print("Valid response:")
    print(good.model_dump())
    print("First tool called:", good.tool_calls[0].name)
    print("-" * 50)

    # 2. Bad input — `reply` must be a string, we gave it an int (123).
    # You might expect 123 to become "123", but Pydantic v2 does NOT coerce
    # a number into a str field. Coercion only runs in the safe direction
    # (text -> number, as in 01). A number landing in a text field usually
    # means something upstream is wrong, so Pydantic flags it instead of
    # silently hiding the bug.
    try:
        AgentResponse(reply=123)
    except ValidationError as exc:
        print("Caught a ValidationError (exactly what we want):")
        print(exc)


if __name__ == "__main__":
    main()
