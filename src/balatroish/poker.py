"""Poker hand evaluation for the protected phase-02 loop."""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from enum import IntEnum

from .cards import Card


class HandRank(IntEnum):
    HIGH_CARD = 1
    PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    STRAIGHT = 5
    FLUSH = 6
    FULL_HOUSE = 7
    FOUR_OF_A_KIND = 8
    STRAIGHT_FLUSH = 9


@dataclass(frozen=True)
class EvaluatedHand:
    rank: HandRank
    tiebreak: tuple[int, ...]


class PokerEvaluator:
    """Evaluates 5-card poker hands.

    Note: kept intentionally readable for early-phase prototype correctness.
    """

    @staticmethod
    def evaluate(hand: list[Card]) -> EvaluatedHand:
        if len(hand) != 5:
            raise ValueError("hand must have exactly 5 cards")

        ranks = sorted((c.rank_value for c in hand), reverse=True)
        counts = Counter(ranks)
        grouped = sorted(counts.items(), key=lambda t: (t[1], t[0]), reverse=True)
        is_flush = len({c.suit for c in hand}) == 1
        is_straight = PokerEvaluator._is_straight(ranks)

        if is_straight and is_flush:
            return EvaluatedHand(HandRank.STRAIGHT_FLUSH, (max(ranks),))
        if grouped[0][1] == 4:
            four = grouped[0][0]
            kicker = grouped[1][0]
            return EvaluatedHand(HandRank.FOUR_OF_A_KIND, (four, kicker))
        if grouped[0][1] == 3 and grouped[1][1] == 2:
            return EvaluatedHand(HandRank.FULL_HOUSE, (grouped[0][0], grouped[1][0]))
        if is_flush:
            return EvaluatedHand(HandRank.FLUSH, tuple(ranks))
        if is_straight:
            return EvaluatedHand(HandRank.STRAIGHT, (max(ranks),))
        if grouped[0][1] == 3:
            kickers = tuple(sorted((r for r in ranks if r != grouped[0][0]), reverse=True))
            return EvaluatedHand(HandRank.THREE_OF_A_KIND, (grouped[0][0],) + kickers)
        if grouped[0][1] == 2 and grouped[1][1] == 2:
            high_pair = max(grouped[0][0], grouped[1][0])
            low_pair = min(grouped[0][0], grouped[1][0])
            kicker = next(r for r in ranks if r not in {high_pair, low_pair})
            return EvaluatedHand(HandRank.TWO_PAIR, (high_pair, low_pair, kicker))
        if grouped[0][1] == 2:
            pair = grouped[0][0]
            kickers = tuple(sorted((r for r in ranks if r != pair), reverse=True))
            return EvaluatedHand(HandRank.PAIR, (pair,) + kickers)
        return EvaluatedHand(HandRank.HIGH_CARD, tuple(ranks))

    @staticmethod
    def _is_straight(ranks_desc: list[int]) -> bool:
        uniq = sorted(set(ranks_desc))
        if len(uniq) != 5:
            return False
        # Wheel straight (A-2-3-4-5)
        if uniq == [2, 3, 4, 5, 14]:
            return True
        return max(uniq) - min(uniq) == 4
