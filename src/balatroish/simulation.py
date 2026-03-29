"""Small simulation helper for early play-loop smoke testing."""

from __future__ import annotations

from .cards import Deck, Suit
from .round_engine import RoundState, RoundEngine
from .sigils import SigilRarity, SuitChipsSigil


def build_default_round_engine(seed: int = 7) -> RoundEngine:
    deck = Deck.standard_52()
    deck.shuffle(seed=seed)
    state = RoundState(
        round_number=1,
        target_score=300,
        deck=deck,
        active_sigils=[
            SuitChipsSigil(name="Heart Ember", rarity=SigilRarity.COMMON, target_suit=Suit.HEARTS, chips_bonus=5)
        ],
    )
    engine = RoundEngine(state)
    engine.enter_round()
    return engine
