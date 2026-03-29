"""Balatroish core package (phase 00-10 implementation scaffold)."""

from .boss_system import BossBlueprint, BossCategory, starter_bosses
from .bosses import BossKind, BossModifier
from .cards import Card, Deck, Suit
from .constellation import ConstellationWeb, NodeType, WeaveNode, WeaveState, default_web
from .design_gate import FeatureProposal, GateResult, evaluate_feature_gate
from .emotion import EmotionalTarget, emotional_target_for_round
from .framework import BossDirector, EnhancementRegistry, Phase0010Framework, SigilRegistry
from .visuals import mermaid_phase_flow, mermaid_runtime_architecture, phase_cards, render_terminal_board, visual_snapshot
from .enhancements import Enhancement, EnhancementKind
from .poker import HandRank, PokerEvaluator
from .round_engine import RoundEngine, RoundPhase, RoundState
from .shop import ShopOffer, ShopState
from .sigils import (
    PairAmplifierSigil,
    Sigil,
    SigilFamily,
    SigilRarity,
    SigilRing,
    SigilState,
    SigilTemplate,
    SuitChipsSigil,
)

__all__ = [
    "BossBlueprint",
    "BossCategory",
    "starter_bosses",
    "BossKind",
    "BossModifier",
    "Card",
    "Deck",
    "Suit",
    "ConstellationWeb",
    "NodeType",
    "WeaveNode",
    "WeaveState",
    "default_web",
    "FeatureProposal",
    "GateResult",
    "evaluate_feature_gate",
    "EmotionalTarget",
    "emotional_target_for_round",
    "Enhancement",
    "EnhancementKind",
    "HandRank",
    "PokerEvaluator",
    "RoundEngine",
    "RoundPhase",
    "RoundState",
    "ShopOffer",
    "ShopState",
    "PairAmplifierSigil",
    "Sigil",
    "SigilFamily",
    "SigilRarity",
    "SigilRing",
    "SigilState",
    "SigilTemplate",
    "SuitChipsSigil",
    "BossDirector",
    "EnhancementRegistry",
    "Phase0010Framework",
    "SigilRegistry",
    "mermaid_phase_flow",
    "mermaid_runtime_architecture",
    "phase_cards",
    "render_terminal_board",
    "visual_snapshot",
]
