from collections.abc import Iterable
from typing import TypeAlias

FromTo: TypeAlias = tuple[str, str]  # (1)

def zip_replace(text: str, changes: Iterable[FromTo]) -> str:  # (2)
    for from_, to in changes:
        text = text.replace(from_, to)
    return text
