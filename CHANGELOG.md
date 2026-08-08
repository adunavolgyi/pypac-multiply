# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
