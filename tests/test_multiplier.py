import pytest

from pypac_multiply import multiplier


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (1, "mono"),
        (2, "di"),
        (3, "tri"),
        (4, "tetra"),
        (8, "octa"),
        (9, "nona"),
        (10, "deca"),
        (20, "icosa"),
        (30, "triaconta"),
        (90, "nonaconta"),
        (100, "hecta"),
        (200, "dicta"),
        (900, "nonacta"),
        (1000, "kilia"),
        (2000, "dilia"),
        (9000, "nonalia"),
    ],
)
def test_fundamental_terms(number: int, expected: str) -> None:
    assert multiplier(number) == expected


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (12, "dodeca"),
        (14, "tetradeca"),
        (21, "henicosa"),
        (22, "docosa"),
        (23, "tricosa"),
        (32, "dotriaconta"),
        (41, "hentetraconta"),
        (52, "dopentaconta"),
        (101, "henhecta"),
        (241, "hentetracontadicta"),
        (363, "trihexacontatricta"),
        (486, "hexaoctacontatetracta"),
        (1001, "henkilia"),
        (1002, "dokilia"),
        (9999, "nonanonacontanonactanonalia"),
    ],
)
def test_compound_terms(number: int, expected: str) -> None:
    assert multiplier(number) == expected


def test_every_supported_number_produces_a_nonempty_ascii_term() -> None:
    terms = [multiplier(number) for number in range(1, 10_000)]

    assert len(set(terms)) == 9999
    assert all(term and term.isascii() and term.isalpha() for term in terms)
