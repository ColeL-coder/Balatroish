import unittest

from src.balatroish.design_gate import FeatureProposal, evaluate_feature_gate


class DesignGateTests(unittest.TestCase):
    def test_accepts_aligned_feature(self):
        proposal = FeatureProposal(
            name="Sigil adjacency resonance",
            deepens_poker_decisions=True,
            strengthens_sigil_identity=True,
            preserves_mobile_readability=True,
            maintains_round_pace=True,
            described_system_tags=("sigil_ring",),
        )
        result = evaluate_feature_gate(proposal)
        self.assertTrue(result.accepted)
        self.assertEqual(result.reasons, ())

    def test_rejects_excluded_system(self):
        proposal = FeatureProposal(
            name="Battlefield mode",
            deepens_poker_decisions=False,
            strengthens_sigil_identity=False,
            preserves_mobile_readability=False,
            maintains_round_pace=False,
            described_system_tags=("tactical_battlefields",),
        )
        result = evaluate_feature_gate(proposal)
        self.assertFalse(result.accepted)
        self.assertTrue(any("scope boundaries" in reason for reason in result.reasons))


if __name__ == "__main__":
    unittest.main()
