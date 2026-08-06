import pytest

from pypac_multiply import multiplier


@pytest.mark.parametrize("number", [0, -1, -9999, 10_000, 10_001])
def test_out_of_range_values(number: int) -> None:
    with pytest.raises(ValueError, match="between 1 and 9999"):
        multiplier(number)


@pytest.mark.parametrize("value", [True, False, 4.2, "21", None, 2 + 0j])
def test_invalid_types(value: object) -> None:
    with pytest.raises(TypeError, match="must be an integer"):
        multiplier(value)  # type: ignore[arg-type]
