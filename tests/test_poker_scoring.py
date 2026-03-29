import unittest

from src.balatroish.cards import Card, Suit
from src.balatroish.poker import PokerEvaluator, HandRank
from src.balatroish.scoring import score_hand


class PokerScoringTests(unittest.TestCase):
    def test_straight_flush(self):
        hand = [
            Card("10", Suit.HEARTS),
            Card("J", Suit.HEARTS),
            Card("Q", Suit.HEARTS),
            Card("K", Suit.HEARTS),
            Card("A", Suit.HEARTS),
        ]
        evaluated = PokerEvaluator.evaluate(hand)
        self.assertEqual(evaluated.rank, HandRank.STRAIGHT_FLUSH)

    def test_pair_scoring(self):
        hand = [
            Card("A", Suit.HEARTS),
            Card("A", Suit.CLUBS),
            Card("9", Suit.SPADES),
            Card("6", Suit.DIAMONDS),
            Card("3", Suit.HEARTS),
        ]
        evaluated = PokerEvaluator.evaluate(hand)
        breakdown = score_hand(evaluated, sigil_bonus_chips=5, sigil_bonus_mult=1)
        self.assertEqual(evaluated.rank, HandRank.PAIR)
        self.assertEqual(breakdown.chips, 15)
        self.assertEqual(breakdown.mult, 2)
        self.assertEqual(breakdown.total, 30)


if __name__ == "__main__":
    unittest.main()
