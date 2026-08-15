"""Construct basic and complex IUPAC multiplicative prefixes.

The implementation follows IUPAC Blue Book (2013), P-14.2.1 through P-14.2.2.
"""

# Compositional 0-99 stems for the hot path; standalone 1 and 2 are special-cased.
_LOW = (
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
    "deca",
    "undeca",
    "dodeca",
    "trideca",
    "tetradeca",
    "pentadeca",
    "hexadeca",
    "heptadeca",
    "octadeca",
    "nonadeca",
    "icosa",
    "henicosa",
    "docosa",
    "tricosa",
    "tetracosa",
    "pentacosa",
    "hexacosa",
    "heptacosa",
    "octacosa",
    "nonacosa",
    "triaconta",
    "hentriaconta",
    "dotriaconta",
    "tritriaconta",
    "tetratriaconta",
    "pentatriaconta",
    "hexatriaconta",
    "heptatriaconta",
    "octatriaconta",
    "nonatriaconta",
    "tetraconta",
    "hentetraconta",
    "dotetraconta",
    "tritetraconta",
    "tetratetraconta",
    "pentatetraconta",
    "hexatetraconta",
    "heptatetraconta",
    "octatetraconta",
    "nonatetraconta",
    "pentaconta",
    "henpentaconta",
    "dopentaconta",
    "tripentaconta",
    "tetrapentaconta",
    "pentapentaconta",
    "hexapentaconta",
    "heptapentaconta",
    "octapentaconta",
    "nonapentaconta",
    "hexaconta",
    "henhexaconta",
    "dohexaconta",
    "trihexaconta",
    "tetrahexaconta",
    "pentahexaconta",
    "hexahexaconta",
    "heptahexaconta",
    "octahexaconta",
    "nonahexaconta",
    "heptaconta",
    "henheptaconta",
    "doheptaconta",
    "triheptaconta",
    "tetraheptaconta",
    "pentaheptaconta",
    "hexaheptaconta",
    "heptaheptaconta",
    "octaheptaconta",
    "nonaheptaconta",
    "octaconta",
    "henoctaconta",
    "dooctaconta",
    "trioctaconta",
    "tetraoctaconta",
    "pentaoctaconta",
    "hexaoctaconta",
    "heptaoctaconta",
    "octaoctaconta",
    "nonaoctaconta",
    "nonaconta",
    "hennonaconta",
    "dononaconta",
    "trinonaconta",
    "tetranonaconta",
    "pentanonaconta",
    "hexanonaconta",
    "heptanonaconta",
    "octanonaconta",
    "nonanonaconta",
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


def multiplier(number: int, *, complex: bool = False) -> str:
    """Return an IUPAC numerical multiplier for ``number``.

    Args:
        number: A built-in integer from 1 through 9999 (inclusive). Integer
            subclasses, including :class:`bool`, are not accepted.
        complex: Return the form for compound or complex features. This must
            be a boolean and defaults to ``False``.

    Raises:
        TypeError: If ``number`` is not a built-in integer or ``complex`` is
            not a boolean.
        ValueError: If ``number`` is outside the supported range.
    """
    if type(number) is not int:
        raise TypeError("number must be a built-in int")
    if complex is False:
        if not 1 <= number <= 9999:
            raise ValueError("number must be between 1 and 9999")
        if number == 1:
            return "mono"
        if number == 2:
            return "di"
        if number < 100:
            return _LOW[number]
    else:
        if complex is not True:
            raise TypeError("complex must be a bool")
        if not 1 <= number <= 9999:
            raise ValueError("number must be between 1 and 9999")
        # P-14.2.2 defines no distinct complex counterpart to mono.
        if number == 1:
            return "mono"
        if number == 2:
            return "bis"
        if number == 3:
            return "tris"
        if number < 100:
            return _LOW[number] + "kis"

    low_part = _LOW[number % 100]
    hundreds_part = _HUNDREDS[number // 100 % 10]
    thousands_part = _THOUSANDS[number // 1000]

    if complex:
        return f"{low_part}{hundreds_part}{thousands_part}kis"
    return f"{low_part}{hundreds_part}{thousands_part}"
