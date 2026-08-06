import pytest

from pypac_multiply import multiplier


class IntSubclass(int):
    pass


@pytest.mark.parametrize(
    "number", [0, -1, -9999, 10_000, 10_001, -(10**1000), 10**1000]
)
def test_out_of_range_values(number: int) -> None:
    with pytest.raises(ValueError, match="between 1 and 9999"):
        multiplier(number)


@pytest.mark.parametrize(
    "value", [True, False, IntSubclass(21), 4.2, "21", None, 2 + 0j]
)
def test_invalid_types(value: object) -> None:
    with pytest.raises(TypeError, match="must be a built-in int"):
        multiplier(value)  # type: ignore[arg-type]
