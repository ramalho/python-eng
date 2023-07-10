from pytest import mark

from messages import show_count


@mark.parametrize(
    'qty, expected',
    [
        (1, '1 part'),
        (2, '2 parts'),
    ],
)
def test_show_count(qty: int, expected: str) -> None:
    got = show_count(qty, 'part')
    assert got == expected


def test_show_count_zero() -> None:
    got = show_count(0, 'part')
    assert got == 'no parts'


def test_irregular() -> None:
    got = show_count(2, 'child', 'children')
    assert got == '2 children'
