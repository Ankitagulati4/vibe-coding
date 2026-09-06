"""
SLIDE 5 · PART 1 · PYDANTIC — Give your data a shape
-----------------------------------------------------
Pydantic parses AND validates your data in a single step.
This is the backbone of every agent tool input/output.

RUN:  python 01_pydantic_basics.py
"""

from pydantic import BaseModel, Field


class WeatherQuery(BaseModel):
    city: str
    country: str = Field(default="IN")        # default value
    units: str = "celsius"
    days: int = 1                             # a NUMBER field, to show coercion


def main() -> None:
    # We only pass `city` — the rest fall back to their defaults.
    query = WeatherQuery(city="Hyderabad")

    print("As a model :", query)
    print("As a dict  :", query.model_dump())
    print("As JSON    :", query.model_dump_json())

    # Coercion happens ONLY in the safe direction: text that clearly
    # represents a number -> a real number.
    # `days` expects an int. We pass the TEXT "3" on purpose, and Pydantic
    # converts it into the number 3 because "3" unambiguously means three.
    # (Note: the reverse — a number into a str field — is NOT auto-converted;
    #  see 02_pydantic_validation.py for why.)
    coerced = WeatherQuery(city="Delhi", days="3")
    print("Coerced    :", coerced.model_dump())
    print("days type  :", type(coerced.days).__name__, "-> value:", coerced.days)


if __name__ == "__main__":
    main()
