import pytest

from pypac_multiply import multiplier


class IntSubclass(int):
    pass


@pytest.mark.parametrize(
    ("number", "expected"),
    [
        (2, "bis"),
        (3, "tris"),
        (4, "tetrakis"),
        (5, "pentakis"),
        (6, "hexakis"),
        (7, "heptakis"),
        (8, "octakis"),
        (9, "nonakis"),
        (10, "decakis"),
        (11, "undecakis"),
        (12, "dodecakis"),
        (20, "icosakis"),
        (21, "henicosakis"),
        (22, "docosakis"),
        (100, "hectakis"),
        (231, "hentriacontadictakis"),
        (1001, "henkiliakis"),
        (9999, "nonanonacontanonactanonaliakis"),
    ],
)
def test_complex_terms(number: int, expected: str) -> None:
    assert multiplier(number, complex=True) == expected


def test_every_supported_complex_term_is_unique_and_systematic() -> None:
    terms = [multiplier(number, complex=True) for number in range(2, 10_000)]

    assert len(set(terms)) == 9998
    assert terms[0:2] == ["bis", "tris"]
    assert all(
        multiplier(number, complex=True) == f"{multiplier(number)}kis"
        for number in range(4, 10_000)
    )


@pytest.mark.parametrize("number", [1, 0, -1, 10_000, 10**1000])
def test_complex_out_of_range_values(number: int) -> None:
    with pytest.raises(ValueError, match="between 2 and 9999"):
        multiplier(number, complex=True)


@pytest.mark.parametrize("value", [True, False, IntSubclass(4), 4.2, "4", None, 4 + 0j])
def test_complex_form_rejects_invalid_number_types(value: object) -> None:
    with pytest.raises(TypeError, match="must be a built-in int"):
        multiplier(value, complex=True)  # type: ignore[arg-type]


@pytest.mark.parametrize("value", [0, 1, "yes", None])
def test_complex_option_requires_a_bool(value: object) -> None:
    with pytest.raises(TypeError, match="complex must be a bool"):
        multiplier(4, complex=value)  # type: ignore[arg-type]


def test_complex_option_is_keyword_only() -> None:
    with pytest.raises(TypeError):
        multiplier(4, True)  # type: ignore[call-arg]
