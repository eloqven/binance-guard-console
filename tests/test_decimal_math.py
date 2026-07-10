from decimal import Decimal

import pytest

from binance_guard_console.decimal_math import (
    format_decimal,
    is_increment_aligned,
    round_down_to_increment,
    round_up_to_increment,
    to_decimal,
)


def test_to_decimal_accepts_safe_inputs() -> None:
    assert to_decimal("1.2300") == Decimal("1.2300")
    assert to_decimal(12) == Decimal("12")
    assert to_decimal(Decimal("0.000001")) == Decimal("0.000001")


@pytest.mark.parametrize("value", [1.1, True, False])
def test_to_decimal_rejects_binary_float_and_boolean_inputs(value: object) -> None:
    with pytest.raises(TypeError):
        to_decimal(value)  # type: ignore[arg-type]


@pytest.mark.parametrize("value", ["NaN", "Infinity", "-Infinity"])
def test_to_decimal_rejects_non_finite_values(value: str) -> None:
    with pytest.raises(ValueError, match="finite"):
        to_decimal(value)


def test_round_down_to_increment() -> None:
    assert round_down_to_increment("1.23456", "0.001") == Decimal("1.234")
    assert round_down_to_increment("1.23000", "0.001") == Decimal("1.230")
    assert round_down_to_increment("0.000000019", "0.00000001") == Decimal("0.00000001")


def test_round_up_to_increment() -> None:
    assert round_up_to_increment("1.23401", "0.001") == Decimal("1.235")
    assert round_up_to_increment("1.23000", "0.001") == Decimal("1.230")
    assert round_up_to_increment("0.000000011", "0.00000001") == Decimal("0.00000002")


@pytest.mark.parametrize("increment", ["0", "-0.01"])
def test_rounding_rejects_non_positive_increment(increment: str) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        round_down_to_increment("1", increment)


def test_rounding_rejects_negative_executable_value() -> None:
    with pytest.raises(ValueError, match="non-negative"):
        round_up_to_increment("-1", "0.01")


def test_increment_alignment_is_exact() -> None:
    assert is_increment_aligned("2.50", "0.05") is True
    assert is_increment_aligned("2.51", "0.05") is False


def test_format_decimal_avoids_scientific_notation_and_redundant_zeros() -> None:
    assert format_decimal("1E-8") == "0.00000001"
    assert format_decimal("12.340000") == "12.34"
    assert format_decimal("100") == "100"
    assert format_decimal("0.000") == "0"
    assert format_decimal("-0.000") == "0"
