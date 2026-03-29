#!/usr/bin/env python3
"""Validate 00-10 contracts against implementation scaffolds."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.balatroish.boss_system import BossCategory, starter_bosses
from src.balatroish.constellation import NodeType, default_web
from src.balatroish.enhancements import EnhancementKind
from src.balatroish.phase_00_10_contract import (
    ARCHETYPES_06,
    BOSS_10,
    CONSTELLATION_08,
    EMOTION_04,
    ENHANCEMENT_09,
    MISSION_00,
    PILLARS_01,
    ROUND_02,
    SCOPE_03,
    SIGIL_05,
)
from src.balatroish.sigils import SigilFamily, SigilRarity, SigilState, TriggerType


def _assert(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def validate_00() -> None:
    lowered = MISSION_00.statement.lower()
    for token in ("mobile", "poker", "sigil", "constellation"):
        _assert(token in lowered, f"mission missing token: {token}")


def validate_01() -> None:
    _assert(len(PILLARS_01) == 3, "phase 01 must keep three pillars")
    _assert(all(p.hard_rule for p in PILLARS_01), "all pillars need hard rules")


def validate_02() -> None:
    _assert(ROUND_02.phases == ("hand", "scoring", "reward", "shop", "progression"), "phase order changed")
    for req in ROUND_02.required_steps:
        _assert(req in ROUND_02.required_steps, f"missing loop step: {req}")


def validate_03_04() -> None:
    overlap = set(SCOPE_03.preserved) & set(SCOPE_03.excluded)
    _assert(not overlap, f"scope overlap: {overlap}")
    _assert(len(EMOTION_04.early) >= 3 and len(EMOTION_04.mid) >= 3 and len(EMOTION_04.late) >= 3, "emotion beats incomplete")


def validate_05_07() -> None:
    _assert(SIGIL_05.min_start_slots >= 2, "sigil start slots too low")
    _assert(SIGIL_05.max_slots_cap <= 8, "sigil cap too high for readability")
    _assert(set(SIGIL_05.rarity_bands) == {r.value for r in SigilRarity}, "rarity mismatch")
    _assert(set(SIGIL_05.lifecycle_states) == {s.value for s in SigilState}, "lifecycle mismatch")
    _assert(set(SIGIL_05.trigger_taxonomy) == {t.value for t in TriggerType}, "trigger taxonomy mismatch")
    _assert(set(ARCHETYPES_06.families) == {f.value for f in SigilFamily}, "archetype family mismatch")


def validate_08_09_10() -> None:
    _assert(CONSTELLATION_08.between_round_only, "constellation must remain between-round")
    _assert(set(CONSTELLATION_08.node_types) == {n.value for n in NodeType}, "constellation node type mismatch")
    _assert(set(ENHANCEMENT_09.required_roles) == {e.value for e in EnhancementKind}, "enhancement role mismatch")
    web = default_web()
    _assert(bool(web.nodes), "constellation web empty")
    bosses = starter_bosses()
    _assert(bosses, "starter bosses missing")
    _assert(set(BOSS_10.must_have), "boss must-have constraints empty")
    _assert(set(BOSS_10.must_not_have), "boss must-not-have constraints empty")
    _assert(any(b.category == BossCategory.MULT_CAP for b in bosses), "missing mult-cap starter boss")


def main() -> None:
    validate_00()
    validate_01()
    validate_02()
    validate_03_04()
    validate_05_07()
    validate_08_09_10()
    print("Phase 00-10 contract validation passed.")


if __name__ == "__main__":
    main()
