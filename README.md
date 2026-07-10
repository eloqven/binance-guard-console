# Binance Guard Console

A local, defensive Binance Spot decision-support and OCO-protection system.

The guard begins as a **dry-run-first tool**, not an auto-trader:

```text
Scan → Signal → Confirm fill → Build exact OCO → Validate → Dry-run/place → Track outcome
```

## Safety contract

1. Dry-run is the default and only permitted mode at repository birth.
2. No live entry orders in v1.
3. No OCO without a confirmed fill.
4. No executable price or quantity math using binary floating point.
5. No order construction without current Binance symbol filters.
6. No new trade while an existing position is unprotected.
7. Ambiguous exchange or account state pauses the system instead of guessing.
8. Every decision, validation failure, and state transition must be explainable and logged.
9. API credentials must never be committed.
10. Live-order capabilities require explicit, separate safety gates and tests.

## Current status

Day 2 adds deterministic `Decimal` helpers for future Binance prices and quantities:

- safe conversion from strings, integers, and `Decimal` values;
- explicit rejection of binary floats and non-finite numbers;
- exact round-down and round-up operations for tick and step increments;
- increment-alignment checks;
- plain-decimal formatting without exponent notation or signed zero.

The repository still contains no Binance client and cannot place any order.

## Local setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
pytest
ruff check .
python -m binance_guard_console
```

## Decimal arithmetic example

```python
from binance_guard_console.decimal_math import (
    format_decimal,
    round_down_to_increment,
)

price = round_down_to_increment("1.23456", "0.001")
assert format_decimal(price) == "1.234"
```
