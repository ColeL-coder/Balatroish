"""Phase-04 emotional arc helper."""

from __future__ import annotations

from dataclasses import dataclass

from .phase_00_04_contract import EMOTIONAL_ARC


@dataclass(frozen=True)
class EmotionalTarget:
    stage: str
    beats: tuple[str, ...]


def emotional_target_for_round(round_number: int, total_rounds: int = 12) -> EmotionalTarget:
    if round_number < 1:
        raise ValueError("round_number must be >= 1")
    if round_number <= total_rounds // 3:
        return EmotionalTarget(stage="early", beats=EMOTIONAL_ARC.early)
    if round_number <= (2 * total_rounds) // 3:
        return EmotionalTarget(stage="mid", beats=EMOTIONAL_ARC.mid)
    return EmotionalTarget(stage="late", beats=EMOTIONAL_ARC.late)
