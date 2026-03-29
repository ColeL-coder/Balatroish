"""Phase-01 feature gate and phase-03 scope boundary checks."""

from __future__ import annotations

from dataclasses import dataclass

from .phase_00_04_contract import EXCLUDED_SYSTEMS


@dataclass(frozen=True)
class FeatureProposal:
    name: str
    deepens_poker_decisions: bool
    strengthens_sigil_identity: bool
    preserves_mobile_readability: bool
    maintains_round_pace: bool
    described_system_tags: tuple[str, ...] = ()


@dataclass(frozen=True)
class GateResult:
    accepted: bool
    reasons: tuple[str, ...]


def evaluate_feature_gate(proposal: FeatureProposal) -> GateResult:
    reasons: list[str] = []

    if not proposal.deepens_poker_decisions:
        reasons.append("fails pillar: poker-core decision quality")
    if not proposal.strengthens_sigil_identity:
        reasons.append("fails pillar: sigil identity")
    if not proposal.preserves_mobile_readability:
        reasons.append("fails pillar: portrait-mobile readability")
    if not proposal.maintains_round_pace:
        reasons.append("fails pillar: round pace / cognitive load")

    excluded = set(EXCLUDED_SYSTEMS)
    overlap = sorted(excluded.intersection(proposal.described_system_tags))
    if overlap:
        reasons.append(f"violates scope boundaries: {', '.join(overlap)}")

    return GateResult(accepted=not reasons, reasons=tuple(reasons))
