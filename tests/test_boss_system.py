import unittest

from src.balatroish.boss_system import starter_bosses


class BossSystemTests(unittest.TestCase):
    def test_starter_bosses_validate(self):
        bosses = starter_bosses()
        self.assertGreaterEqual(len(bosses), 2)
        self.assertTrue(all(b.counterplay for b in bosses))


if __name__ == "__main__":
    unittest.main()
