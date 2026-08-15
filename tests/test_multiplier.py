import pytest

from pypac_multiply import multiplier

_REFERENCE_UNITS = (
    "",
    "hen",
    "do",
    "tri",
    "tetra",
    "penta",
    "hexa",
    "hepta",
    "octa",
    "nona",
)
_REFERENCE_TENS = (
    "",
    "deca",
    "icosa",
    "triaconta",
    "tetraconta",
    "pentaconta",
    "hexaconta",
    "heptaconta",
    "octaconta",
    "nonaconta",
)
_REFERENCE_HUNDREDS = (
    "",
    "hecta",
    "dicta",
    "tricta",
    "tetracta",
    "pentacta",
    "hexacta",
    "heptacta",
    "octacta",
    "nonacta",
)
_REFERENCE_THOUSANDS = (
    "",
    "kilia",
    "dilia",
    "trilia",
    "tetralia",
    "pentalia",
    "hexalia",
    "heptalia",
    "octalia",
    "nonalia",
)


def _reference_multiplier(number: int) -> str:
    if number == 1:
        return "mono"
    if number == 2:
        return "di"

    units = number % 10
    tens = number // 10 % 10
    low = "undeca" if units == tens == 1 else _REFERENCE_UNITS[units]
    if units != 1 or tens != 1:
        low += "cosa" if tens == 2 and units >= 2 else _REFERENCE_TENS[tens]

    return (
        low
        + _REFERENCE_HUNDREDS[number // 100 % 10]
        + _REFERENCE_THOUSANDS[number // 1000]
    )


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, "mono"),
        (2, "di"),
        (3, "tri"),
        (4, "tetra"),
        (5, "penta"),
        (6, "hexa"),
        (7, "hepta"),
        (8, "octa"),
        (9, "nona"),
        (10, "deca"),
        (11, "undeca"),
        (20, "icosa"),
        (30, "triaconta"),
        (40, "tetraconta"),
        (50, "pentaconta"),
        (60, "hexaconta"),
        (70, "heptaconta"),
        (80, "octaconta"),
        (90, "nonaconta"),
        (100, "hecta"),
        (200, "dicta"),
        (300, "tricta"),
        (400, "tetracta"),
        (500, "pentacta"),
        (600, "hexacta"),
        (700, "heptacta"),
        (800, "octacta"),
        (900, "nonacta"),
        (1000, "kilia"),
        (2000, "dilia"),
        (3000, "trilia"),
        (4000, "tetralia"),
        (5000, "pentalia"),
        (6000, "hexalia"),
        (7000, "heptalia"),
        (8000, "octalia"),
        (9000, "nonalia"),
    ],
)
def test_blue_book_table_terms(number: int, expected: str) -> None:
    assert multiplier(number) == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (14, "tetradeca"),
        (21, "henicosa"),
        (22, "docosa"),
        (23, "tricosa"),
        (24, "tetracosa"),
        (41, "hentetraconta"),
        (52, "dopentaconta"),
        (111, "undecahecta"),
        (363, "trihexacontatricta"),
        (486, "hexaoctacontatetracta"),
    ],
)
def test_blue_book_examples(number: int, expected: str) -> None:
    assert multiplier(number) == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (12, "dodeca"),
        (32, "dotriaconta"),
        (101, "henhecta"),
        (241, "hentetracontadicta"),
        (1001, "henkilia"),
        (1002, "dokilia"),
        (9999, "nonanonacontanonactanonalia"),
    ],
)
def test_additional_compound_terms(number: int, expected: str) -> None:
    assert multiplier(number) == expected


def test_every_supported_number_produces_a_nonempty_ascii_term() -> None:
    terms = [multiplier(number) for number in range(1, 10_000)]

    assert len(set(terms)) == 9999
    assert all(term and term.isascii() and term.isalpha() for term in terms)


def test_every_supported_number_matches_the_reference_rules() -> None:
    assert all(
        multiplier(number) == _reference_multiplier(number)
        for number in range(1, 10_000)
    )
