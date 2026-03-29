"""Simple shop system for prototype loop."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ShopOffer:
    key: str
    title: str
    cost: int
    description: str


@dataclass
class ShopState:
    offers: list[ShopOffer]

    def buy(self, key: str, money: int) -> tuple[int, ShopOffer]:
        offer = next((o for o in self.offers if o.key == key), None)
        if offer is None:
            raise ValueError(f"unknown offer: {key}")
        if money < offer.cost:
            raise ValueError("insufficient funds")
        self.offers = [o for o in self.offers if o.key != key]
        return money - offer.cost, offer
