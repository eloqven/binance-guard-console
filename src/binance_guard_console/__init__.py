"""Binance Guard Console foundation package."""

from .safety import GuardMode, SafetyContract, default_safety_contract

__all__ = ["GuardMode", "SafetyContract", "default_safety_contract"]
__version__ = "0.1.0"
