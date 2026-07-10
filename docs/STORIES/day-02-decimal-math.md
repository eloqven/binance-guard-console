# Day 2 — Decimal-safe exchange arithmetic

## Goal

Create the exact arithmetic foundation required for Binance Spot prices and quantities.

## Scope

- Parse user and exchange values into `Decimal` without binary-float leakage.
- Round prices and quantities down to an exchange increment.
- Round values up to an exchange increment when a safety relationship requires it.
- Detect whether a value is aligned to an increment.
- Format executable values without scientific notation.
- Reject non-positive increments, negative executable values, booleans, floats, and non-finite values.
- Add unit tests covering ordinary and pathological inputs.

## Acceptance criteria

- No executable arithmetic uses `float`.
- `round_down_to_increment("1.23456", "0.001")` produces `Decimal("1.234")`.
- `round_up_to_increment("1.23401", "0.001")` produces `Decimal("1.235")`.
- Exact multiples remain unchanged.
- Scientific-notation input is accepted but formatted as plain decimal text.
- Invalid values and increments fail explicitly.
- All existing tests remain green.

## Out of scope

- Binance HTTP access.
- `exchangeInfo` parsing.
- OCO construction.
- Live or paper orders.

## Safety note

This story adds only pure deterministic math helpers. It introduces no network access and no trading capability.
