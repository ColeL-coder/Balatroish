import unittest

from src.balatroish.bosses import BossKind, BossModifier
from src.balatroish.cards import Card, Suit
from src.balatroish.poker import HandRank
from src.balatroish.sigils import (
    PairAmplifierSigil,
    SigilRarity,
    SuitChipsSigil,
    combine_sigil_results,
)


class SigilAndBossTests(unittest.TestCase):
    def test_suit_sigil_adds_chips(self):
        hand = [
            Card("A", Suit.HEARTS),
            Card("4", Suit.CLUBS),
            Card("6", Suit.SPADES),
            Card("8", Suit.DIAMONDS),
            Card("J", Suit.CLUBS),
        ]
        sigil = SuitChipsSigil(name="Heart Ember", rarity=SigilRarity.COMMON, target_suit=Suit.HEARTS, chips_bonus=7)
        result = sigil.apply(hand, HandRank.HIGH_CARD)
        self.assertEqual(result.bonus_chips, 7)

    def test_pair_sigil_adds_mult(self):
        sigil = PairAmplifierSigil(name="Twin Echo", rarity=SigilRarity.REFINED, mult_bonus=2)
        result = sigil.apply([], HandRank.PAIR)
        self.assertEqual(result.bonus_mult, 2)

    def test_combine_sigil_results(self):
        s1 = SuitChipsSigil(name="Heart Ember", rarity=SigilRarity.COMMON, chips_bonus=4)
        s2 = PairAmplifierSigil(name="Twin Echo", rarity=SigilRarity.REFINED, mult_bonus=1)
        c1 = s1.apply([Card("2", Suit.HEARTS)], HandRank.HIGH_CARD)
        c2 = s2.apply([], HandRank.PAIR)
        combined = combine_sigil_results([c1, c2])
        self.assertEqual(combined.bonus_chips, 4)
        self.assertEqual(combined.bonus_mult, 1)

    def test_boss_mult_cap(self):
        boss = BossModifier(kind=BossKind.MULT_CAP, mult_cap=3)
        self.assertEqual(boss.clamp_mult(8), 3)


if __name__ == "__main__":
    unittest.main()
