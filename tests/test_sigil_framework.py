import unittest

from src.balatroish.cards import Card, Suit
from src.balatroish.constellation import WeaveState, default_web
from src.balatroish.poker import HandRank
from src.balatroish.sigils import (
    SigilFamily,
    SigilRarity,
    SigilRing,
    SigilTemplate,
    TriggerType,
    PairAmplifierSigil,
)


class SigilFrameworkTests(unittest.TestCase):
    def test_template_validation(self):
        template = SigilTemplate(
            name="Twin Echo",
            family=SigilFamily.ECHO,
            rarity=SigilRarity.REFINED,
            visual_description="Looped crystal glyph",
            trigger=TriggerType.HAND_TYPE,
            short_effect_text="+1 mult on Pair or better",
            long_effect_text="Whenever you score Pair+, gain +1 mult.",
            scaling_note="Awakened grants +2",
            synergy_hooks=("pair_build",),
            weaknesses=("high_card_hands",),
        )
        template.validate()

    def test_ring_aggregation(self):
        ring = SigilRing(max_slots=2)
        ring.equip(PairAmplifierSigil(name="Twin Echo", rarity=SigilRarity.COMMON, mult_bonus=1))
        result = ring.total_bonus([Card("A", Suit.HEARTS)], HandRank.PAIR)
        self.assertEqual(result.bonus_mult, 1)

    def test_constellation_unlock(self):
        web = default_web()
        state = WeaveState(starlight=5)
        web.unlock("root", state)
        self.assertIn("root", state.unlocked)


if __name__ == "__main__":
    unittest.main()
