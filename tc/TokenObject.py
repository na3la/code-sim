from dataclasses import dataclass

"""
This is a simple dataclass definition of a TokenObject.
"""


@dataclass(init=True, repr=True, eq=True)
class TokenObject:
    token: str
    value: str
