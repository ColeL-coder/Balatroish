"""Phase 00-04 executable design contract.

This module converts the design docs into machine-checkable structures so
future implementation work can validate drift against the intended core.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MissionContract:
    statement: str
    must_include: tuple[str, ...]


@dataclass(frozen=True)
class PillarContract:
    name: str
    hard_rule: str


@dataclass(frozen=True)
class EmotionalArc:
    early: tuple[str, ...]
    mid: tuple[str, ...]
    late: tuple[str, ...]


MISSION = MissionContract(
    statement=(
        "Design a mobile-first roguelike poker deckbuilder that preserves "
        "chips × multiplier hand-scoring, differentiates through Sigils, "
        "and uses Constellation Weaving as support without replacing poker."
    ),
    must_include=("mobile-first", "poker", "Sigils", "Constellation Weaving"),
)

PILLARS = (
    PillarContract(
        name="Familiar Poker Core",
        hard_rule="Never add mechanics that make poker-hand evaluation secondary.",
    ),
    PillarContract(
        name="Sigils as Identity Engine",
        hard_rule="If a Sigil is replaceable by a generic passive, redesign it.",
    ),
    PillarContract(
        name="Premium Portrait-Mobile Spectacle",
        hard_rule="If spectacle hurts clarity, clarity wins.",
    ),
)

CORE_LOOP = (
    "enter_round",
    "draw_cards",
    "form_poker_hand",
    "play_or_discard",
    "score_chips_x_mult",
    "beat_threshold",
    "earn_rewards",
    "visit_shop",
    "improve_deck_or_sigils",
    "face_harder_rounds",
)

PRESERVED_SYSTEMS = (
    "recognizable_poker_hands",
    "chips_and_multiplier_language",
    "escalating_targets",
    "deck_curation_and_trimming",
    "shop_decision_pressure",
    "boss_disruption_rounds",
)

EXCLUDED_SYSTEMS = (
    "tactical_battlefields",
    "unit_summoning_replacing_poker",
    "long_in_run_skill_trees",
    "currency_sprawl",
    "real_time_mechanics",
    "constellation_minigame",
)

EMOTIONAL_ARC = EmotionalArc(
    early=("curiosity", "mystical discovery", "direction finding"),
    mid=("control", "elegance", "engine building"),
    late=("spectacle", "inevitability", "beautiful chaos"),
)
