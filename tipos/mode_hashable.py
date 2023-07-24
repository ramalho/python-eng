from collections import Counter
from collections.abc import Iterable, Hashable
from typing import TypeVar, TYPE_CHECKING

HashableT = TypeVar('HashableT', bound=Hashable)

def mode(data: Iterable[HashableT]) -> HashableT:
    pairs = Counter(data).most_common(1)
    if len(pairs) == 0:
        raise ValueError('no mode for empty data')
    return pairs[0][0]


m = mode([3, 4, 1, 3, 1, 3, 3, 2])

if TYPE_CHECKING:
    reveal_type(m)

print(m)

print(m * 10)
