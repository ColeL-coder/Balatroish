"""Phase-02 round engine scaffold.

Implements the protected round structure:
hand -> score -> reward -> shop -> progression.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from .bosses import BossModifier
from .cards import Deck, Card
from .enhancements import Enhancement
from .poker import PokerEvaluator
from .scoring import score_hand, ScoreBreakdown
from .sigils import Sigil, combine_sigil_results


class RoundPhase(str, Enum):
    HAND = "hand"
    SCORING = "scoring"
    REWARD = "reward"
    SHOP = "shop"
    PROGRESSION = "progression"


@dataclass
class RoundState:
    round_number: int
    target_score: int
    deck: Deck
    hand_size: int = 8
    hands_remaining: int = 4
    discards_remaining: int = 4
    money: int = 0
    score_total: int = 0
    phase: RoundPhase = RoundPhase.HAND
    current_draw: list[Card] = field(default_factory=list)
    active_sigils: list[Sigil] = field(default_factory=list)
    boss_modifier: BossModifier | None = None
    event_log: list[str] = field(default_factory=list)
    card_enhancements: dict[int, Enhancement] = field(default_factory=dict)


class RoundEngine:
    def __init__(self, state: RoundState):
        self.state = state

    def _draw_refill(self, count: int) -> list[Card]:
        if len(self.state.deck.cards) < count:
            # reshuffle from standard set for prototype continuity
            refill = Deck.standard_52()
            refill.shuffle(seed=self.state.round_number)
            self.state.deck.cards.extend(refill.cards)
        return self.state.deck.draw(count)

    def enter_round(self) -> None:
        self.state.phase = RoundPhase.HAND
        self.state.current_draw = self._draw_refill(self.state.hand_size)
        self.state.event_log.append(f"round_{self.state.round_number}:enter")

    def discard_and_redraw(self, indexes: list[int]) -> None:
        if self.state.phase != RoundPhase.HAND:
            raise RuntimeError("discard_and_redraw can only be used during HAND phase")
        if self.state.discards_remaining <= 0:
            raise RuntimeError("no discards remaining")

        for i in sorted(indexes, reverse=True):
            if i < 0 or i >= len(self.state.current_draw):
                raise IndexError("discard index out of range")
            self.state.current_draw.pop(i)
        self.state.current_draw.extend(self._draw_refill(len(indexes)))
        self.state.discards_remaining -= 1
        self.state.event_log.append(f"round_{self.state.round_number}:discard_{len(indexes)}")

    def play_hand(self, indexes: list[int], sigil_bonus_chips: int = 0, sigil_bonus_mult: int = 0) -> ScoreBreakdown:
        if self.state.phase != RoundPhase.HAND:
            raise RuntimeError("play_hand can only be used during HAND phase")
        if len(indexes) != 5:
            raise ValueError("exactly 5 cards are required")

        hand = [self.state.current_draw[i] for i in indexes]
        evaluated = PokerEvaluator.evaluate(hand)

        sigil_results = [sigil.apply(hand, evaluated.rank) for sigil in self.state.active_sigils]
        combined = combine_sigil_results(sigil_results)

        enh_chips = 0
        enh_mult = 0
        for idx in indexes:
            enh = self.state.card_enhancements.get(idx)
            if enh is None:
                continue
            chips, mult, _economy = enh.apply_to_card(self.state.current_draw[idx])
            enh_chips += chips
            enh_mult += mult

        total_bonus_chips = sigil_bonus_chips + combined.bonus_chips + enh_chips
        total_bonus_mult = sigil_bonus_mult + combined.bonus_mult + enh_mult
        if self.state.boss_modifier:
            total_bonus_chips -= self.state.boss_modifier.chips_penalty(hand)

        breakdown = score_hand(
            evaluated,
            sigil_bonus_chips=total_bonus_chips,
            sigil_bonus_mult=total_bonus_mult,
        )

        if self.state.boss_modifier:
            clamped_mult = self.state.boss_modifier.clamp_mult(breakdown.mult)
            if clamped_mult != breakdown.mult:
                breakdown = ScoreBreakdown(
                    hand_rank=breakdown.hand_rank,
                    base_chips=breakdown.chips,
                    base_mult=clamped_mult,
                    sigil_bonus_chips=0,
                    sigil_bonus_mult=0,
                )

        self.state.score_total += breakdown.total
        self.state.hands_remaining -= 1
        self.state.phase = RoundPhase.SCORING
        self.state.event_log.append(
            f"round_{self.state.round_number}:play:{evaluated.rank.name}:total_{breakdown.total}"
        )
        return breakdown

    def resolve_scoring(self) -> None:
        if self.state.phase != RoundPhase.SCORING:
            raise RuntimeError("resolve_scoring can only be used during SCORING phase")
        self.state.phase = RoundPhase.REWARD

    def claim_reward(self, money_gain: int) -> None:
        if self.state.phase != RoundPhase.REWARD:
            raise RuntimeError("claim_reward can only be used during REWARD phase")
        self.state.money += money_gain
        self.state.phase = RoundPhase.SHOP

    def leave_shop(self, spend: int = 0) -> None:
        if self.state.phase != RoundPhase.SHOP:
            raise RuntimeError("leave_shop can only be used during SHOP phase")
        if spend > self.state.money:
            raise ValueError("cannot spend more money than available")
        self.state.money -= spend
        self.state.phase = RoundPhase.PROGRESSION

    def progress(self) -> bool:
        if self.state.phase != RoundPhase.PROGRESSION:
            raise RuntimeError("progress can only be used during PROGRESSION phase")

        passed = self.state.score_total >= self.state.target_score
        self.state.round_number += 1
        self.state.target_score = int(self.state.target_score * 1.35)
        self.state.score_total = 0
        self.state.hands_remaining = 4
        self.state.discards_remaining = 4
        self.state.phase = RoundPhase.HAND
        self.state.current_draw = self._draw_refill(self.state.hand_size)
        self.state.event_log.append(f"round_{self.state.round_number}:progress:{'pass' if passed else 'fail'}")
        return passed
