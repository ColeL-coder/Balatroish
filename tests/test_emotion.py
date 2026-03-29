import unittest

from src.balatroish.emotion import emotional_target_for_round


class EmotionTests(unittest.TestCase):
    def test_early_mid_late(self):
        self.assertEqual(emotional_target_for_round(1, total_rounds=12).stage, "early")
        self.assertEqual(emotional_target_for_round(6, total_rounds=12).stage, "mid")
        self.assertEqual(emotional_target_for_round(11, total_rounds=12).stage, "late")


if __name__ == "__main__":
    unittest.main()
