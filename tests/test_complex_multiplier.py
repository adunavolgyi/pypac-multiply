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
        (231, "hentriacontadictakis"),
    ],
)
def test_blue_book_complex_examples(number: int, expected: str) -> None:
    assert multiplier(number, complex=True) == expected


def test_complex_one_uses_basic_fallback_by_package_policy() -> None:
    assert multiplier(1, complex=True) == "mono"


@pytest.mark.parametrize(
    ("number", "expected"),
    [
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
        (1001, "henkiliakis"),
        (9999, "nonanonacontanonactanonaliakis"),
    ],
)
def test_additional_complex_terms(number: int, expected: str) -> None:
    assert multiplier(number, complex=True) == expected


def test_every_supported_complex_term_is_unique_and_well_formed() -> None:
    terms = [multiplier(number, complex=True) for number in range(1, 10_000)]

    assert len(set(terms)) == 9999
    assert terms[0:3] == ["mono", "bis", "tris"]
    assert all(term.isascii() and term.isalpha() for term in terms)


def test_complex_terms_use_the_systematic_suffix_after_special_cases() -> None:
    assert all(
        multiplier(number, complex=True) == f"{multiplier(number)}kis"
        for number in range(4, 10_000)
    )


@pytest.mark.parametrize("number", [0, -1, 10_000, 10**1000])
def test_complex_out_of_range_values(number: int) -> None:
    with pytest.raises(ValueError, match="between 1 and 9999"):
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
