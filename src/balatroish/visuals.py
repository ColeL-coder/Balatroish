"""Visual helpers for phase 00-10 planning artifacts.

No GUI here yet; we generate markdown/mermaid and terminal-friendly status boards.
"""

from __future__ import annotations

from dataclasses import dataclass

from .framework import Phase0010Framework


@dataclass(frozen=True)
class PhaseCard:
    phase: str
    title: str
    status: str


def phase_cards() -> tuple[PhaseCard, ...]:
    return (
        PhaseCard("00", "Mission Brief", "implemented"),
        PhaseCard("01", "Foundation Lock", "implemented"),
        PhaseCard("02", "Round Structure", "implemented"),
        PhaseCard("03", "Scope Boundaries", "implemented"),
        PhaseCard("04", "Emotional Fantasy", "implemented"),
        PhaseCard("05", "Sigil Framework", "implemented"),
        PhaseCard("06", "Sigil Archetypes", "implemented"),
        PhaseCard("07", "Sigil Templates", "implemented"),
        PhaseCard("08", "Constellation Weaving", "implemented"),
        PhaseCard("09", "Enhancement Rules", "implemented"),
        PhaseCard("10", "Boss Philosophy", "implemented"),
    )


def render_terminal_board() -> str:
    lines = ["Phase 00-10 Status Board", "=" * 28]
    for card in phase_cards():
        lines.append(f"[{card.phase}] {card.title:<24} :: {card.status}")
    return "\n".join(lines)


def mermaid_phase_flow() -> str:
    return """```mermaid
flowchart LR
  P00[00 Mission] --> P01[01 Pillars]
  P01 --> P02[02 Round Flow]
  P02 --> P03[03 Scope]
  P03 --> P04[04 Emotional Arc]
  P04 --> P05[05 Sigil Framework]
  P05 --> P06[06 Archetypes]
  P06 --> P07[07 Templates]
  P07 --> P08[08 Constellation]
  P08 --> P09[09 Enhancements]
  P09 --> P10[10 Boss Philosophy]
```"""


def mermaid_runtime_architecture() -> str:
    return """```mermaid
graph TD
  F[Phase0010Framework] --> SR[SigilRegistry]
  F --> ER[EnhancementRegistry]
  F --> BD[BossDirector]
  F --> CW[ConstellationWeb]
  F --> R[RoundEngine]
  R --> S[Scoring]
  R --> SG[Sigils]
  R --> B[Boss Modifier]
  R --> E[Enhancements]
```"""


def visual_snapshot(framework: Phase0010Framework) -> str:
    sigils = len(framework.sigil_registry.templates)
    enhancements = len(framework.enhancement_registry.catalog)
    bosses = len(framework.boss_director.pool)
    weave_nodes = len(framework.constellation.nodes)
    return (
        f"Mission: {framework.mission_statement}\n"
        f"Archetypes: {len(framework.archetype_families)}\n"
        f"Sigil templates: {sigils}\n"
        f"Enhancement types: {enhancements}\n"
        f"Boss blueprints: {bosses}\n"
        f"Constellation nodes: {weave_nodes}"
    )
