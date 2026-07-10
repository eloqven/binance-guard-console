"""Minimal Day 1 command-line status output."""

from __future__ import annotations

from .safety import default_safety_contract


def main() -> None:
    contract = default_safety_contract()
    print("Binance Guard Console")
    print(f"mode={contract.mode.value}")
    print("live_entry=disabled")
    print("live_oco=disabled")
    print("status=foundation-safe")


if __name__ == "__main__":
    main()
