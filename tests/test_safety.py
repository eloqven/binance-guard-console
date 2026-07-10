from dataclasses import replace

import pytest

from binance_guard_console.safety import GuardMode, default_safety_contract


def test_default_contract_is_dry_run_and_valid() -> None:
    contract = default_safety_contract()

    assert contract.mode is GuardMode.DRY_RUN
    assert contract.allow_live_entry is False
    assert contract.allow_live_oco is False
    assert contract.pause_on_ambiguous_state is True
    assert contract.require_confirmed_fill_before_oco is True
    assert contract.require_current_exchange_filters is True


@pytest.mark.parametrize(
    ("field", "unsafe_value", "message"),
    [
        ("allow_live_entry", True, "Live entry is forbidden"),
        ("allow_live_oco", True, "Live OCO placement is forbidden"),
        ("pause_on_ambiguous_state", False, "Ambiguous exchange state"),
        ("require_confirmed_fill_before_oco", False, "confirmed fill"),
        ("require_current_exchange_filters", False, "current exchange filters"),
    ],
)
def test_contract_rejects_unsafe_foundation_overrides(
    field: str,
    unsafe_value: bool,
    message: str,
) -> None:
    unsafe_contract = replace(default_safety_contract(), **{field: unsafe_value})

    with pytest.raises(ValueError, match=message):
        unsafe_contract.validate()
