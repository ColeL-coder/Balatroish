"""Prototype boss disruptions for early rounds."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .cards import Card, Suit


class BossKind(str, Enum):
    SUIT_SUPPRESSION = "suit_suppression"
    MULT_CAP = "mult_cap"


@dataclass(frozen=True)
class BossModifier:
    kind: BossKind
    target_suit: Suit | None = None
    mult_cap: int | None = None

    def chips_penalty(self, hand: list[Card]) -> int:
        if self.kind == BossKind.SUIT_SUPPRESSION and self.target_suit is not None:
            return sum(3 for c in hand if c.suit == self.target_suit)
        return 0

    def clamp_mult(self, current_mult: int) -> int:
        if self.kind == BossKind.MULT_CAP and self.mult_cap is not None:
            return min(current_mult, self.mult_cap)
        return current_mult
