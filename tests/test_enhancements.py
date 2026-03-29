import unittest

from src.balatroish.cards import Card, Suit
from src.balatroish.enhancements import Enhancement, EnhancementKind


class EnhancementsTests(unittest.TestCase):
    def test_gilded_bonus(self):
        enh = Enhancement(kind=EnhancementKind.GILDED, chips_bonus=1)
        chips, mult, econ = enh.apply_to_card(Card("A", Suit.HEARTS))
        self.assertEqual((chips, mult, econ), (3, 0, 1))


if __name__ == "__main__":
    unittest.main()
