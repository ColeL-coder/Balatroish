#!/usr/bin/env python3
"""Validate phase 00-04 design contracts.

Run this script in CI or pre-implementation checkpoints to detect mission drift.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.balatroish.phase_00_04_contract import (
    CORE_LOOP,
    EMOTIONAL_ARC,
    EXCLUDED_SYSTEMS,
    MISSION,
    PILLARS,
    PRESERVED_SYSTEMS,
)


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_mission() -> None:
    lowered = MISSION.statement.lower()
    for token in MISSION.must_include:
        _assert(token.lower() in lowered, f"Mission missing required token: {token}")


def validate_pillars() -> None:
    _assert(len(PILLARS) == 3, "Expected exactly three non-negotiable pillars")
    for pillar in PILLARS:
        _assert(bool(pillar.hard_rule.strip()), f"Missing hard rule for pillar: {pillar.name}")


def validate_core_loop() -> None:
    required_steps = {"draw_cards", "form_poker_hand", "score_chips_x_mult", "visit_shop"}
    _assert(required_steps.issubset(set(CORE_LOOP)), "Core loop missing protected essentials")
    _assert(len(CORE_LOOP) >= 10, "Core loop should keep full round cadence")


def validate_scope_boundaries() -> None:
    _assert(len(PRESERVED_SYSTEMS) >= 6, "Preserved systems list is incomplete")
    _assert(len(EXCLUDED_SYSTEMS) >= 6, "Excluded systems list is incomplete")
    overlap = set(PRESERVED_SYSTEMS) & set(EXCLUDED_SYSTEMS)
    _assert(not overlap, f"Preserved/excluded overlap detected: {sorted(overlap)}")


def validate_emotional_arc() -> None:
    _assert(len(EMOTIONAL_ARC.early) >= 3, "Early emotional beats incomplete")
    _assert(len(EMOTIONAL_ARC.mid) >= 3, "Mid emotional beats incomplete")
    _assert(len(EMOTIONAL_ARC.late) >= 3, "Late emotional beats incomplete")


def main() -> None:
    validate_mission()
    validate_pillars()
    validate_core_loop()
    validate_scope_boundaries()
    validate_emotional_arc()
    print("Phase 00-04 contract validation passed.")


if __name__ == "__main__":
    main()
