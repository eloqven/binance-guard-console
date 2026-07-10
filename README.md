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

## Day 1 status

The repository contains only foundation code and safety configuration. Nothing can connect to Binance or place an order.

## Local setup

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e ".[dev]"
pytest
python -m binance_guard_console
```
