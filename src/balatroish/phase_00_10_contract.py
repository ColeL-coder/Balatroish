"""Executable contract for phases 00-10 (mission through boss philosophy)."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Mission:
    statement: str
    identity_points: tuple[str, ...]


@dataclass(frozen=True)
class Pillar:
    name: str
    hard_rule: str


@dataclass(frozen=True)
class RoundStructure:
    phases: tuple[str, ...]
    required_steps: tuple[str, ...]


@dataclass(frozen=True)
class ScopeBoundary:
    preserved: tuple[str, ...]
    excluded: tuple[str, ...]


@dataclass(frozen=True)
class EmotionalArcContract:
    early: tuple[str, ...]
    mid: tuple[str, ...]
    late: tuple[str, ...]


@dataclass(frozen=True)
class SigilFrameworkContract:
    min_start_slots: int
    max_slots_cap: int
    rarity_bands: tuple[str, ...]
    lifecycle_states: tuple[str, ...]
    trigger_taxonomy: tuple[str, ...]


@dataclass(frozen=True)
class ArchetypeContract:
    families: tuple[str, ...]


@dataclass(frozen=True)
class ConstellationContract:
    node_types: tuple[str, ...]
    between_round_only: bool


@dataclass(frozen=True)
class EnhancementContract:
    required_roles: tuple[str, ...]


@dataclass(frozen=True)
class BossPhilosophyContract:
    must_have: tuple[str, ...]
    must_not_have: tuple[str, ...]


MISSION_00 = Mission(
    statement=(
        "Design a mobile-first roguelike poker deckbuilder with Sigils as the core "
        "identity layer and Constellation Weaving as support that never replaces poker."
    ),
    identity_points=("poker_core", "sigils_primary", "mobile_readability", "premium_celestial_tone"),
)

PILLARS_01 = (
    Pillar("Familiar Poker Core", "Never make poker-hand evaluation secondary."),
    Pillar("Sigils Identity Engine", "If Sigils are replaceable by generic passives, redesign."),
    Pillar("Portrait-Mobile Clarity", "If spectacle hurts clarity, clarity wins."),
)

ROUND_02 = RoundStructure(
    phases=("hand", "scoring", "reward", "shop", "progression"),
    required_steps=("draw_cards", "form_poker_hand", "score_chips_x_mult", "visit_shop"),
)

SCOPE_03 = ScopeBoundary(
    preserved=(
        "recognizable_poker_hands",
        "chips_multiplier_language",
        "escalating_targets",
        "deck_curation",
        "shop_pressure",
        "boss_disruption",
    ),
    excluded=(
        "tactical_battlefields",
        "unit_summoning",
        "long_skill_trees",
        "currency_sprawl",
        "real_time_mechanics",
        "constellation_minigame",
    ),
)

EMOTION_04 = EmotionalArcContract(
    early=("curiosity", "mystical_discovery", "direction_finding"),
    mid=("control", "elegance", "engine_building"),
    late=("spectacle", "inevitability", "beautiful_chaos"),
)

SIGIL_05 = SigilFrameworkContract(
    min_start_slots=3,
    max_slots_cap=6,
    rarity_bands=("common", "refined", "rare", "mythic", "celestial", "corrupt"),
    lifecycle_states=("dormant", "bound", "awakened", "exalted", "corrupted", "fused", "split", "shattered"),
    trigger_taxonomy=(
        "hand_type",
        "suit_match",
        "rank_match",
        "first_hand",
        "repeat_hand",
        "discard_discipline",
        "enhancement_present",
        "boss_interaction",
    ),
)

ARCHETYPES_06 = ArchetypeContract(
    families=(
        "suit",
        "rank",
        "echo",
        "alchemy",
        "chaos",
        "harmony",
        "corruption",
        "celestial",
        "combo_chain",
        "precision",
    )
)

CONSTELLATION_08 = ConstellationContract(
    node_types=(
        "sigil_charge",
        "suit_affinity",
        "enhancement_chance",
        "corruption_resist",
        "economy_bonus",
        "awakening_reduction",
        "boss_counterplay",
        "retrigger_chance",
    ),
    between_round_only=True,
)

ENHANCEMENT_09 = EnhancementContract(
    required_roles=(
        "gilded",
        "burning",
        "frozen",
        "mirrored",
        "radiant",
        "fractured",
        "thorned",
        "inked",
        "hollow",
        "cursed",
    )
)

BOSS_10 = BossPhilosophyContract(
    must_have=("telegraph", "single_assumption_counter", "counterplay_path", "tension_without_theft"),
    must_not_have=("hard_no_answer_counter", "hidden_core_rules", "confusion_over_friction"),
)
