from dataclasses import dataclass


@dataclass(init=True, repr=True, eq=True)
class TokenObject:
    token: str
    value: str
