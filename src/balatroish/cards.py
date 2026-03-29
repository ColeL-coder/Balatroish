"""Card and deck primitives for Balatroish prototype."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import random


class Suit(str, Enum):
    HEARTS = "H"
    DIAMONDS = "D"
    CLUBS = "C"
    SPADES = "S"


RANK_ORDER = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}


@dataclass(frozen=True)
class Card:
    rank: str
    suit: Suit

    @property
    def rank_value(self) -> int:
        return RANK_ORDER[self.rank]

    @property
    def is_face(self) -> bool:
        return self.rank in {"J", "Q", "K"}


@dataclass
class Deck:
    cards: list[Card]

    @classmethod
    def standard_52(cls) -> "Deck":
        cards = [Card(rank=r, suit=s) for s in Suit for r in RANK_ORDER]
        return cls(cards=cards)

    def shuffle(self, seed: int | None = None) -> None:
        rng = random.Random(seed)
        rng.shuffle(self.cards)

    def draw(self, count: int) -> list[Card]:
        drawn = self.cards[:count]
        self.cards = self.cards[count:]
        return drawn

    def add(self, card: Card) -> None:
        self.cards.append(card)
