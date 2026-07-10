"""Exact decimal helpers for executable exchange values.

Prices and quantities sent to an exchange must not pass through binary floating
point. This module accepts only strings, integers, and ``Decimal`` instances,
then keeps every calculation in base-10 arithmetic.
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation, ROUND_CEILING, ROUND_FLOOR
from typing import TypeAlias

DecimalInput: TypeAlias = Decimal | int | str


def to_decimal(value: DecimalInput, *, name: str = "value") -> Decimal:
    """Convert a safe input to a finite ``Decimal``.

    ``float`` and ``bool`` values are rejected deliberately. A float may already
    contain binary approximation error before this function sees it, while bool
    is an ``int`` subclass and would otherwise silently become 0 or 1.
    """

    if isinstance(value, bool):
        raise TypeError(f"{name} must not be a boolean")
    if isinstance(value, float):
        raise TypeError(f"{name} must not be a float; pass a string or Decimal")

    try:
        decimal_value = value if isinstance(value, Decimal) else Decimal(value)
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"{name} is not a valid decimal value") from exc

    if not decimal_value.is_finite():
        raise ValueError(f"{name} must be finite")

    return decimal_value


def _validated_non_negative(value: DecimalInput, *, name: str) -> Decimal:
    decimal_value = to_decimal(value, name=name)
    if decimal_value < 0:
        raise ValueError(f"{name} must be non-negative")
    return decimal_value


def _validated_increment(increment: DecimalInput) -> Decimal:
    decimal_increment = to_decimal(increment, name="increment")
    if decimal_increment <= 0:
        raise ValueError("increment must be greater than zero")
    return decimal_increment


def round_down_to_increment(value: DecimalInput, increment: DecimalInput) -> Decimal:
    """Round a non-negative value down to the nearest exact increment."""

    decimal_value = _validated_non_negative(value, name="value")
    decimal_increment = _validated_increment(increment)
    units = (decimal_value / decimal_increment).to_integral_value(rounding=ROUND_FLOOR)
    return units * decimal_increment


def round_up_to_increment(value: DecimalInput, increment: DecimalInput) -> Decimal:
    """Round a non-negative value up to the nearest exact increment."""

    decimal_value = _validated_non_negative(value, name="value")
    decimal_increment = _validated_increment(increment)
    units = (decimal_value / decimal_increment).to_integral_value(rounding=ROUND_CEILING)
    return units * decimal_increment


def is_increment_aligned(value: DecimalInput, increment: DecimalInput) -> bool:
    """Return whether a non-negative value is an exact multiple of an increment."""

    decimal_value = _validated_non_negative(value, name="value")
    decimal_increment = _validated_increment(increment)
    return decimal_value % decimal_increment == 0


def format_decimal(value: DecimalInput) -> str:
    """Format a finite decimal without exponent notation or redundant zeros."""

    decimal_value = to_decimal(value)
    text = format(decimal_value, "f")

    if "." in text:
        text = text.rstrip("0").rstrip(".")

    return text or "0"
