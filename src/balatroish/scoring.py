"""Scoring language: chips × multiplier."""

from __future__ import annotations

from dataclasses import dataclass

from .poker import HandRank, EvaluatedHand


BASE_CHIPS = {
    HandRank.HIGH_CARD: 5,
    HandRank.PAIR: 10,
    HandRank.TWO_PAIR: 20,
    HandRank.THREE_OF_A_KIND: 30,
    HandRank.STRAIGHT: 40,
    HandRank.FLUSH: 45,
    HandRank.FULL_HOUSE: 60,
    HandRank.FOUR_OF_A_KIND: 80,
    HandRank.STRAIGHT_FLUSH: 120,
}

BASE_MULT = {
    HandRank.HIGH_CARD: 1,
    HandRank.PAIR: 1,
    HandRank.TWO_PAIR: 2,
    HandRank.THREE_OF_A_KIND: 2,
    HandRank.STRAIGHT: 3,
    HandRank.FLUSH: 3,
    HandRank.FULL_HOUSE: 4,
    HandRank.FOUR_OF_A_KIND: 6,
    HandRank.STRAIGHT_FLUSH: 10,
}


@dataclass(frozen=True)
class ScoreBreakdown:
    hand_rank: HandRank
    base_chips: int
    base_mult: int
    sigil_bonus_chips: int
    sigil_bonus_mult: int

    @property
    def chips(self) -> int:
        return self.base_chips + self.sigil_bonus_chips

    @property
    def mult(self) -> int:
        return self.base_mult + self.sigil_bonus_mult

    @property
    def total(self) -> int:
        return self.chips * self.mult


def score_hand(evaluated: EvaluatedHand, sigil_bonus_chips: int = 0, sigil_bonus_mult: int = 0) -> ScoreBreakdown:
    return ScoreBreakdown(
        hand_rank=evaluated.rank,
        base_chips=BASE_CHIPS[evaluated.rank],
        base_mult=BASE_MULT[evaluated.rank],
        sigil_bonus_chips=sigil_bonus_chips,
        sigil_bonus_mult=sigil_bonus_mult,
    )
