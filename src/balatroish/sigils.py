"""Phase 05-07 Sigil framework: slots, families, lifecycle, and templates."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .cards import Card, Suit
from .poker import HandRank


class SigilRarity(str, Enum):
    COMMON = "common"
    REFINED = "refined"
    RARE = "rare"
    MYTHIC = "mythic"
    CELESTIAL = "celestial"
    CORRUPT = "corrupt"


class SigilFamily(str, Enum):
    SUIT = "suit"
    RANK = "rank"
    ECHO = "echo"
    ALCHEMY = "alchemy"
    CHAOS = "chaos"
    HARMONY = "harmony"
    CORRUPTION = "corruption"
    CELESTIAL = "celestial"
    COMBO_CHAIN = "combo_chain"
    PRECISION = "precision"


class SigilState(str, Enum):
    DORMANT = "dormant"
    BOUND = "bound"
    AWAKENED = "awakened"
    EXALTED = "exalted"
    CORRUPTED = "corrupted"
    SPLIT = "split"
    FUSED = "fused"
    SHATTERED = "shattered"


class TriggerType(str, Enum):
    HAND_TYPE = "hand_type"
    SUIT_MATCH = "suit_match"
    RANK_MATCH = "rank_match"
    FIRST_HAND = "first_hand"
    REPEAT_HAND = "repeat_hand"
    DISCARD_DISCIPLINE = "discard_discipline"
    ENHANCEMENT_PRESENT = "enhancement_present"
    BOSS_INTERACTION = "boss_interaction"


@dataclass(frozen=True)
class SigilResult:
    bonus_chips: int = 0
    bonus_mult: int = 0


@dataclass(frozen=True)
class SigilTemplate:
    name: str
    family: SigilFamily
    rarity: SigilRarity
    visual_description: str
    trigger: TriggerType
    short_effect_text: str
    long_effect_text: str
    scaling_note: str
    synergy_hooks: tuple[str, ...]
    weaknesses: tuple[str, ...]

    def validate(self) -> None:
        if len(self.short_effect_text) > 90:
            raise ValueError("short_effect_text should remain mobile concise")
        if not self.visual_description.strip():
            raise ValueError("visual_description is required")
        if not self.synergy_hooks:
            raise ValueError("at least one synergy hook is required")


@dataclass(frozen=True)
class Sigil:
    name: str
    family: SigilFamily
    rarity: SigilRarity
    state: SigilState = SigilState.BOUND
    level: int = 1

    def apply(self, hand: list[Card], hand_rank: HandRank) -> SigilResult:  # pragma: no cover - interface
        return SigilResult()


@dataclass(frozen=True)
class SuitChipsSigil(Sigil):
    family: SigilFamily = field(default=SigilFamily.SUIT, init=False)
    target_suit: Suit = Suit.HEARTS
    chips_bonus: int = 8

    def apply(self, hand: list[Card], hand_rank: HandRank) -> SigilResult:
        bonus = self.chips_bonus + max(0, self.level - 1)
        if any(card.suit == self.target_suit for card in hand):
            return SigilResult(bonus_chips=bonus)
        return SigilResult()


@dataclass(frozen=True)
class PairAmplifierSigil(Sigil):
    family: SigilFamily = field(default=SigilFamily.ECHO, init=False)
    mult_bonus: int = 1

    def apply(self, hand: list[Card], hand_rank: HandRank) -> SigilResult:
        if hand_rank >= HandRank.PAIR:
            bonus = self.mult_bonus + (1 if self.state in {SigilState.AWAKENED, SigilState.EXALTED} else 0)
            return SigilResult(bonus_mult=bonus)
        return SigilResult()


@dataclass
class SigilRing:
    max_slots: int = 3
    slots: list[Sigil] = field(default_factory=list)

    def equip(self, sigil: Sigil) -> None:
        if len(self.slots) >= self.max_slots:
            raise ValueError("sigil ring full")
        self.slots.append(sigil)

    def expand(self, extra_slots: int = 1) -> None:
        self.max_slots += extra_slots

    def total_bonus(self, hand: list[Card], hand_rank: HandRank) -> SigilResult:
        return combine_sigil_results([sigil.apply(hand, hand_rank) for sigil in self.slots])


def combine_sigil_results(results: list[SigilResult]) -> SigilResult:
    return SigilResult(
        bonus_chips=sum(r.bonus_chips for r in results),
        bonus_mult=sum(r.bonus_mult for r in results),
    )
