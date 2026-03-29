"""Phase 10 boss philosophy + category data model."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class BossCategory(str, Enum):
    SUIT_SUPPRESSION = "suit_suppression"
    REPETITION_PUNISH = "repetition_punish"
    MULT_CAP = "mult_cap"
    CORRUPTION_PRESSURE = "corruption_pressure"
    SIGIL_SILENCE = "sigil_silence"
    ENHANCEMENT_SCRAMBLE = "enhancement_scramble"
    RANK_DISTORTION = "rank_distortion"
    CELESTIAL_INTERFERENCE = "celestial_interference"
    TIMING_SEQUENCE = "timing_sequence"


@dataclass(frozen=True)
class BossBlueprint:
    key: str
    category: BossCategory
    title: str
    telegraph: str
    disruption: str
    counterplay: tuple[str, ...]

    def validate(self) -> None:
        if len(self.counterplay) == 0:
            raise ValueError("boss must include at least one counterplay option")
        if not self.telegraph.strip():
            raise ValueError("boss telegraph is required")


def starter_bosses() -> tuple[BossBlueprint, ...]:
    bosses = (
        BossBlueprint(
            key="veil_of_thorns",
            category=BossCategory.SUIT_SUPPRESSION,
            title="Veil of Thorns",
            telegraph="Hearts are weakened this round.",
            disruption="Hearts lose chips contribution when scored.",
            counterplay=("pivot_suit", "rank_build", "boss_ward"),
        ),
        BossBlueprint(
            key="iron_lens",
            category=BossCategory.MULT_CAP,
            title="Iron Lens",
            telegraph="Multiplier is capped this round.",
            disruption="Final multiplier cannot exceed cap value.",
            counterplay=("chips_scaling", "ward_item", "precision_route"),
        ),
    )
    for b in bosses:
        b.validate()
    return bosses
