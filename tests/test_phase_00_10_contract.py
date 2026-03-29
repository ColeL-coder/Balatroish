import unittest

from src.balatroish.phase_00_10_contract import (
    ARCHETYPES_06,
    BOSS_10,
    CONSTELLATION_08,
    ENHANCEMENT_09,
    MISSION_00,
    PILLARS_01,
    ROUND_02,
    SIGIL_05,
)


class Phase0010ContractTests(unittest.TestCase):
    def test_phase_00_has_core_tokens(self):
        text = MISSION_00.statement.lower()
        for token in ("mobile", "poker", "sigil", "constellation"):
            self.assertIn(token, text)

    def test_phase_01_has_three_pillars(self):
        self.assertEqual(len(PILLARS_01), 3)

    def test_phase_02_structure(self):
        self.assertEqual(ROUND_02.phases, ("hand", "scoring", "reward", "shop", "progression"))

    def test_phase_05_06_08_09_10_payloads_present(self):
        self.assertGreaterEqual(SIGIL_05.min_start_slots, 2)
        self.assertIn("echo", ARCHETYPES_06.families)
        self.assertTrue(CONSTELLATION_08.between_round_only)
        self.assertIn("gilded", ENHANCEMENT_09.required_roles)
        self.assertTrue(BOSS_10.must_have)


if __name__ == "__main__":
    unittest.main()
