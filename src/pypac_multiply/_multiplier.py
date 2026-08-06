"""Construct basic IUPAC multiplicative prefixes.

The implementation follows IUPAC Blue Book (2013), P-14.2.1, especially
P-14.2.1.1 (special forms) and P-14.2.1.2 (systematic construction).
"""

_UNITS = (
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
_TENS = (
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
_HUNDREDS = (
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
_THOUSANDS = (
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


def multiplier(number: int) -> str:
    """Return the basic IUPAC numerical multiplier for ``number``.

    Args:
        number: A built-in integer from 1 through 9999 (inclusive). Integer
            subclasses, including :class:`bool`, are not accepted.

    Raises:
        TypeError: If ``number`` is not a built-in integer.
        ValueError: If ``number`` is outside the supported range.
    """
    if type(number) is not int:
        raise TypeError("number must be a built-in int")
    if not 1 <= number <= 9999:
        raise ValueError("number must be between 1 and 9999")

    if number == 1:
        return "mono"
    if number == 2:
        return "di"
    units = number % 10
    tens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000

    hundreds_part = _HUNDREDS[hundreds]
    thousands_part = _THOUSANDS[thousands]

    if units == 1 and tens == 1:
        # P-14.2.1.1.1: eleven is undeca, including inside larger terms.
        return f"undeca{hundreds_part}{thousands_part}"

    units_part = _UNITS[units]
    tens_part = _TENS[tens]
    # P-14.2.1.2: units 2-9 end in a vowel, so elide icosa's initial i.
    if tens == 2 and units >= 2:
        tens_part = "cosa"
    return f"{units_part}{tens_part}{hundreds_part}{thousands_part}"
