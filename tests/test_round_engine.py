import unittest

from src.balatroish.bosses import BossKind, BossModifier
from src.balatroish.round_engine import RoundPhase
from src.balatroish.simulation import build_default_round_engine


class RoundEngineTests(unittest.TestCase):
    def test_round_flow(self):
        engine = build_default_round_engine()
        self.assertEqual(engine.state.phase, RoundPhase.HAND)

        engine.discard_and_redraw([0, 1])
        self.assertEqual(engine.state.discards_remaining, 3)

        breakdown = engine.play_hand([0, 1, 2, 3, 4])
        self.assertGreaterEqual(breakdown.total, 5)
        self.assertEqual(engine.state.phase, RoundPhase.SCORING)

        engine.resolve_scoring()
        self.assertEqual(engine.state.phase, RoundPhase.REWARD)

        engine.claim_reward(money_gain=5)
        self.assertEqual(engine.state.money, 5)
        self.assertEqual(engine.state.phase, RoundPhase.SHOP)

        engine.leave_shop(spend=2)
        self.assertEqual(engine.state.money, 3)
        self.assertEqual(engine.state.phase, RoundPhase.PROGRESSION)

        passed = engine.progress()
        self.assertIsInstance(passed, bool)
        self.assertEqual(engine.state.phase, RoundPhase.HAND)
        self.assertTrue(engine.state.event_log)

    def test_boss_modifier_applies(self):
        engine = build_default_round_engine()
        engine.state.boss_modifier = BossModifier(kind=BossKind.MULT_CAP, mult_cap=1)
        breakdown = engine.play_hand([0, 1, 2, 3, 4], sigil_bonus_mult=5)
        self.assertEqual(breakdown.mult, 1)


if __name__ == "__main__":
    unittest.main()
