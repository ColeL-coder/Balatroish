"""Phase 00-10 orchestration framework.

Provides a single integration layer that wires mission contracts, content registries,
and runtime systems into one place for prototype gameplay and tooling.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from .boss_system import BossBlueprint, starter_bosses
from .constellation import ConstellationWeb, default_web
from .enhancements import Enhancement, EnhancementKind
from .phase_00_10_contract import ARCHETYPES_06, MISSION_00
from .sigils import (
    PairAmplifierSigil,
    Sigil,
    SigilRarity,
    SigilRing,
    SigilTemplate,
    SuitChipsSigil,
    TriggerType,
    SigilFamily,
)


@dataclass
class SigilRegistry:
    templates: dict[str, SigilTemplate] = field(default_factory=dict)

    def register(self, template: SigilTemplate) -> None:
        template.validate()
        self.templates[template.name] = template

    def bootstrap_defaults(self) -> None:
        self.register(
            SigilTemplate(
                name="Heart Ember",
                family=SigilFamily.SUIT,
                rarity=SigilRarity.COMMON,
                visual_description="Heart crest in a warm ring",
                trigger=TriggerType.SUIT_MATCH,
                short_effect_text="+chips when Hearts are scored",
                long_effect_text="If hand contains Hearts, gain bonus chips.",
                scaling_note="+1 chip per level",
                synergy_hooks=("suit_build", "gilded_cards"),
                weaknesses=("suit_suppression_boss",),
            )
        )
        self.register(
            SigilTemplate(
                name="Twin Echo",
                family=SigilFamily.ECHO,
                rarity=SigilRarity.REFINED,
                visual_description="Mirror-loop glyph",
                trigger=TriggerType.HAND_TYPE,
                short_effect_text="+mult on Pair or better",
                long_effect_text="Pair+ hands gain additive multiplier.",
                scaling_note="Awakened adds extra mult",
                synergy_hooks=("pair_build", "retrigger_lines"),
                weaknesses=("high_card_rounds",),
            )
        )


@dataclass
class EnhancementRegistry:
    catalog: dict[EnhancementKind, Enhancement] = field(default_factory=dict)

    def bootstrap_defaults(self) -> None:
        self.catalog = {
            kind: Enhancement(kind=kind)
            for kind in EnhancementKind
        }


@dataclass
class BossDirector:
    pool: tuple[BossBlueprint, ...] = field(default_factory=starter_bosses)

    def boss_for_round(self, round_number: int) -> BossBlueprint:
        if not self.pool:
            raise ValueError("boss pool is empty")
        return self.pool[(round_number - 1) % len(self.pool)]


@dataclass
class Phase0010Framework:
    mission_statement: str = MISSION_00.statement
    archetype_families: tuple[str, ...] = ARCHETYPES_06.families
    sigil_registry: SigilRegistry = field(default_factory=SigilRegistry)
    enhancement_registry: EnhancementRegistry = field(default_factory=EnhancementRegistry)
    boss_director: BossDirector = field(default_factory=BossDirector)
    constellation: ConstellationWeb = field(default_factory=default_web)

    def bootstrap(self) -> None:
        self.sigil_registry.bootstrap_defaults()
        self.enhancement_registry.bootstrap_defaults()

    def starter_ring(self) -> SigilRing:
        ring = SigilRing(max_slots=3)
        ring.equip(SuitChipsSigil(name="Heart Ember", rarity=SigilRarity.COMMON, chips_bonus=5))
        ring.equip(PairAmplifierSigil(name="Twin Echo", rarity=SigilRarity.REFINED, mult_bonus=1))
        return ring
