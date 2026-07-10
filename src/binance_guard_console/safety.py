"""Non-negotiable runtime safety gates.

Day 1 deliberately contains no Binance client and no order-placement code.
These types establish invariants that later modules must depend on.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class GuardMode(StrEnum):
    """Supported guard execution modes.

    Only ``DRY_RUN`` exists at repository birth. New modes must be introduced
    through explicit code changes and tests rather than configuration alone.
    """

    DRY_RUN = "dry_run"


@dataclass(frozen=True, slots=True)
class SafetyContract:
    """Immutable safety configuration shared by future guard components."""

    mode: GuardMode
    allow_live_entry: bool
    allow_live_oco: bool
    pause_on_ambiguous_state: bool
    require_confirmed_fill_before_oco: bool
    require_current_exchange_filters: bool

    def validate(self) -> None:
        """Reject any foundation configuration capable of live trading."""

        if self.mode is not GuardMode.DRY_RUN:
            raise ValueError("Foundation mode must remain dry_run")
        if self.allow_live_entry:
            raise ValueError("Live entry is forbidden during the foundation phase")
        if self.allow_live_oco:
            raise ValueError("Live OCO placement is forbidden during the foundation phase")
        if not self.pause_on_ambiguous_state:
            raise ValueError("Ambiguous exchange state must pause the guard")
        if not self.require_confirmed_fill_before_oco:
            raise ValueError("An OCO may only be built after a confirmed fill")
        if not self.require_current_exchange_filters:
            raise ValueError("Executable orders require current exchange filters")


def default_safety_contract() -> SafetyContract:
    """Return and validate the repository's safe foundation defaults."""

    contract = SafetyContract(
        mode=GuardMode.DRY_RUN,
        allow_live_entry=False,
        allow_live_oco=False,
        pause_on_ambiguous_state=True,
        require_confirmed_fill_before_oco=True,
        require_current_exchange_filters=True,
    )
    contract.validate()
    return contract
