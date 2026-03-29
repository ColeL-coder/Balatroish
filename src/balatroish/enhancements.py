"""Phase 09 Card enhancement framework."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

from .cards import Card


class EnhancementKind(str, Enum):
    GILDED = "gilded"
    BURNING = "burning"
    FROZEN = "frozen"
    MIRRORED = "mirrored"
    RADIANT = "radiant"
    FRACTURED = "fractured"
    THORNED = "thorned"
    INKED = "inked"
    HOLLOW = "hollow"
    CURSED = "cursed"


@dataclass(frozen=True)
class Enhancement:
    kind: EnhancementKind
    chips_bonus: int = 0
    mult_bonus: int = 0
    economy_bonus: int = 0

    def apply_to_card(self, card: Card) -> tuple[int, int, int]:
        # returns chips_bonus, mult_bonus, economy_bonus contribution
        if self.kind == EnhancementKind.GILDED:
            return (self.chips_bonus + 2, self.mult_bonus, self.economy_bonus + 1)
        if self.kind == EnhancementKind.BURNING:
            return (self.chips_bonus + 4, self.mult_bonus + 1, self.economy_bonus)
        if self.kind == EnhancementKind.FROZEN:
            return (self.chips_bonus, self.mult_bonus + 1, self.economy_bonus)
        if self.kind == EnhancementKind.HOLLOW:
            return (max(0, self.chips_bonus - 2), self.mult_bonus + 2, self.economy_bonus)
        if self.kind == EnhancementKind.CURSED:
            return (self.chips_bonus + 6, self.mult_bonus + 1, self.economy_bonus - 1)
        return (self.chips_bonus, self.mult_bonus, self.economy_bonus)
