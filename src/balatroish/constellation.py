"""Phase 08 Constellation Weaving support layer."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class NodeType(str, Enum):
    SIGIL_CHARGE = "sigil_charge"
    SUIT_AFFINITY = "suit_affinity"
    ENHANCEMENT_CHANCE = "enhancement_chance"
    CORRUPTION_RESIST = "corruption_resist"
    ECONOMY_BONUS = "economy_bonus"
    AWAKENING_REDUCTION = "awakening_reduction"
    BOSS_COUNTERPLAY = "boss_counterplay"
    RETRIGGER_CHANCE = "retrigger_chance"


@dataclass(frozen=True)
class WeaveNode:
    key: str
    node_type: NodeType
    cost: int
    value: float
    neighbors: tuple[str, ...] = ()


@dataclass
class WeaveState:
    starlight: int = 0
    unlocked: set[str] = field(default_factory=set)


@dataclass
class ConstellationWeb:
    nodes: dict[str, WeaveNode]

    def can_unlock(self, key: str, state: WeaveState) -> bool:
        node = self.nodes[key]
        if key in state.unlocked:
            return False
        if state.starlight < node.cost:
            return False
        if not node.neighbors:
            return True
        return any(n in state.unlocked for n in node.neighbors)

    def unlock(self, key: str, state: WeaveState) -> None:
        if key not in self.nodes:
            raise ValueError(f"unknown node {key}")
        if not self.can_unlock(key, state):
            raise ValueError(f"cannot unlock node {key}")
        node = self.nodes[key]
        state.starlight -= node.cost
        state.unlocked.add(key)


def default_web() -> ConstellationWeb:
    return ConstellationWeb(
        nodes={
            "root": WeaveNode(key="root", node_type=NodeType.SIGIL_CHARGE, cost=2, value=1.0),
            "economy_1": WeaveNode(
                key="economy_1",
                node_type=NodeType.ECONOMY_BONUS,
                cost=3,
                value=0.1,
                neighbors=("root",),
            ),
            "boss_ward_1": WeaveNode(
                key="boss_ward_1",
                node_type=NodeType.BOSS_COUNTERPLAY,
                cost=3,
                value=1.0,
                neighbors=("root",),
            ),
        }
    )
