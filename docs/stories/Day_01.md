# Day 01 — Repository birth and safety contract

## Story

The guard exists, but it is intentionally powerless against the account. Today establishes the package, test runner, dry-run defaults, and immutable rules future trading modules must obey.

## Delivered

- Python `src/` package skeleton.
- Dry-run-only `GuardMode`.
- Immutable `SafetyContract` with fail-closed validation.
- Safe CLI status command.
- Credential-safe `.gitignore` and `.env.example`.
- Unit tests proving unsafe foundation overrides are rejected.

## Acceptance criteria

- `pytest` passes.
- `python -m binance_guard_console` reports `foundation-safe`.
- No dependency or module can call Binance.
- No live mode can be enabled through config alone.
- Ambiguous state is required to pause.

## Explicitly deferred

- Binance HTTP and WebSocket clients.
- API signing.
- Symbol filters.
- Decimal order calculations.
- OCO construction.
- Dashboard work.

## Suggested commit

```text
day-01: repo birth and safety contract
```
