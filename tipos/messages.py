def show_count(count: int, word: str, plural_word: str | None = None) -> str:
    if count == 1:
        return f'1 {word}'
    count_str = str(count) if count else 'no'
    if plural_word:
        return f'{count_str} {plural_word}'
    return f'{count_str} {word}s'
