# Changelog

## Unreleased

### Added

- Initial Python package and project metadata.
- Dry-run-only safety contract.
- Safe status CLI.
- Foundation tests and configuration templates.
- Decimal-safe conversion for executable exchange values.
- Exact increment rounding and alignment helpers for future tick-size and step-size logic.
- Plain decimal formatting without scientific notation or signed zero.
- Day 2 implementation story and arithmetic test coverage.

### Security

- Live entry and OCO placement are structurally unavailable.
- API credentials are ignored by Git.
- Ambiguous exchange state is defined as fail-closed.
- Binary floating-point values are explicitly rejected from executable arithmetic.
