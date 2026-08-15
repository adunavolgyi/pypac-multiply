# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.1] - 2026-08-15

### Changed

- Made complex mode consistent at 1 by returning `mono`, since IUPAC defines
  no distinct complex counterpart for it.
- Accelerated prefix generation with a dense 0-99 lookup and single-allocation
  complex construction.
- Gated PyPI publishing on the full test matrix, exact tag-version matching,
  and an installed-wheel smoke test.

## [0.2.0] - 2026-08-08

### Added

- Complex multiplicative prefixes from 2 through 9999 through the
  `multiplier(..., complex=True)` option.

### Changed

- Reduced allocations and runtime work in the conversion hot path.
- Rejected all integer subclasses to prevent overridden arithmetic from
  bypassing input validation.

## [0.1.1] - 2026-08-06

### Changed

- Synchronized the PyPI and GitHub version numbers.

## [0.1.0] - 2026-08-06

### Added

- Conversion of integers from 1 through 9999 to basic IUPAC multiplicative
  prefixes.
- Type information and validation for unsupported values.

[Unreleased]: https://github.com/adunavolgyi/pypac-multiply/compare/v0.2.1...HEAD
[0.2.1]: https://github.com/adunavolgyi/pypac-multiply/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/adunavolgyi/pypac-multiply/compare/v0.1.1...v0.2.0
[0.1.1]: https://github.com/adunavolgyi/pypac-multiply/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/adunavolgyi/pypac-multiply/releases/tag/v0.1.0
