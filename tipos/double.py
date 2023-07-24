from collections.abc import Sequence
from typing import Any, Protocol, TypeVar, TYPE_CHECKING
from fractions import Fraction

T = TypeVar('T')


class Repetível(Protocol):
    def __mul__(self: T, other: Any) -> T:
        ...

TR = TypeVar('TR', bound=Repetível)

def dobro(x: TR) -> TR:
    return x * 2

x = dobro(2) + 10

if TYPE_CHECKING:
    reveal_type(x)

print(dobro(3.5))

print(dobro('ma'))

print(dobro(Fraction(2, 3)))

print(dobro([1, 2, 3]))

# erro proposital, nunca vai funcionar
# print(dobro(None))
