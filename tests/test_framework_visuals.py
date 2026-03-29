import unittest

from src.balatroish.framework import Phase0010Framework
from src.balatroish.visuals import mermaid_phase_flow, render_terminal_board, visual_snapshot


class FrameworkVisualTests(unittest.TestCase):
    def test_framework_bootstrap(self):
        fw = Phase0010Framework()
        fw.bootstrap()
        self.assertGreaterEqual(len(fw.sigil_registry.templates), 2)
        self.assertGreaterEqual(len(fw.enhancement_registry.catalog), 10)
        ring = fw.starter_ring()
        self.assertEqual(ring.max_slots, 3)

    def test_visual_outputs(self):
        fw = Phase0010Framework()
        fw.bootstrap()
        board = render_terminal_board()
        self.assertIn("Phase 00-10 Status Board", board)
        self.assertIn("P00", mermaid_phase_flow())
        snapshot = visual_snapshot(fw)
        self.assertIn("Sigil templates", snapshot)


if __name__ == "__main__":
    unittest.main()
