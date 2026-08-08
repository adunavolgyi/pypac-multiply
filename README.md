# pypac-multiply

`pypac-multiply` is a small, dependency-free Python library that converts an
integer into a basic or complex IUPAC numerical multiplier prefix.

```python
from pypac_multiply import multiplier

multiplier(1)  # "mono"
multiplier(21)  # "henicosa"
multiplier(32)  # "dotriaconta"
multiplier(241)  # "hentetracontadicta"
multiplier(4, complex=True)  # "tetrakis"
multiplier(231, complex=True)  # "hentriacontadictakis"
```

The package generates terms algorithmically for the complete range covered by
the IUPAC rules, 1 through 9999. It has no runtime dependencies.

## Installation

```console
python -m pip install pypac-multiply
```

## Usage

The public API consists of one function:

```python
def multiplier(number: int, *, complex: bool = False) -> str: ...
```

`number` must be a built-in integer from 1 through 9999. Values outside that
range raise `ValueError`; other types and integer subclasses, including
`bool`, raise `TypeError`.

```python
multiplier(0)  # ValueError
multiplier(4.2)  # TypeError
multiplier(True)  # TypeError
```

Set `complex=True` for compound or complex features, such as substituted
substituents:

```python
multiplier(2, complex=True)  # "bis"
multiplier(3, complex=True)  # "tris"
multiplier(4, complex=True)  # "tetrakis"
multiplier(12, complex=True)  # "dodecakis"
```

The complex form supports 2 through 9999. IUPAC defines no complex counterpart
to `mono`, so `multiplier(1, complex=True)` raises `ValueError`. The `complex`
option is keyword-only and must be a `bool`.

The implementation follows sections P-14.2.1 and P-14.2.2 of the 2013 IUPAC
*Nomenclature of Organic Chemistry* (the Blue Book). Composite terms cite
units before tens, hundreds, and thousands. It also implements the prescribed
exceptional forms for 1, 2, and 11, the `bis` and `tris` complex forms, and the
elision of the initial `i` of `icosa` after a vowel.

One source inconsistency is resolved in favor of the construction rule: Blue
Book Table 1.4 prints `henkilla` for 1001, while the same table defines 1000 as
`kilia` and P-14.2.1.2 requires direct joining. This package therefore returns
`henkilia` for 1001.

## Development

Clone the repository and install the development dependencies using a tool
that supports the standardized dependency-groups table, for example:

```console
python -m pip install --group dev --editable .
```

Then run the checks:

```console
pytest
ruff check .
ruff format --check .
mypy
python -m build
python -m twine check dist/*
```

## References

- [IUPAC Blue Book, P-14.2](https://iupac.qmul.ac.uk/BlueBook/P1.html#1402)
- [IUPAC numerical terms recommendations](https://iupac.qmul.ac.uk/misc/numb.html)
- [PyPA packaging tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

## License

MIT
