from collections.abc import Sequence
from typing import Any

def dobro(x: Any) -> Any:
    return x * 2

print(dobro(2))

print(dobro(3.5))

print(dobro('ma'))

print(dobro([1, 2, 3]))

# erro proposital, nunca vai funcionar
# print(dobro(None))
