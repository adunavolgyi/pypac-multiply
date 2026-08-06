from pypac_multiply import multiplier


def test_one_and_two_use_standalone_forms_only_when_alone() -> None:
    assert multiplier(1) == "mono"
    assert multiplier(2) == "di"
    assert multiplier(101) == "henhecta"
    assert multiplier(102) == "dohecta"


def test_eleven_is_undeca() -> None:
    assert multiplier(11) == "undeca"
    assert multiplier(111) == "undecahecta"
    assert multiplier(1011) == "undecakilia"


def test_icosa_loses_i_only_after_a_vowel() -> None:
    assert multiplier(20) == "icosa"
    assert multiplier(21) == "henicosa"
    assert multiplier(22) == "docosa"
    assert multiplier(28) == "octacosa"
    assert multiplier(120) == "icosahecta"
