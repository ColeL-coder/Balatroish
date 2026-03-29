# Balatroish

Design documentation lives in `docs/design`.

- Design index: `docs/design/README.md`
- Phase 0 mission brief: `docs/design/00_mission_brief.md`
- Phase 1 foundation lock: `docs/design/01_foundation_lock.md`
- Phase 2 round structure: `docs/design/02_round_structure.md`
- Phase 3 scope boundaries: `docs/design/03_scope_and_boundaries.md`
- Phase 4 emotional fantasy: `docs/design/04_emotional_fantasy.md`

## Coding Initiation (Phases 00-04)

Executable design contracts are now scaffolded for phases 00-04:
- Contract module: `src/balatroish/phase_00_04_contract.py`
- Validation script: `scripts/validate_phase_00_04.py`

Run:

```bash
python scripts/validate_phase_00_04.py
python scripts/validate_phase_00_10.py
```


## Prototype Engine (Phase 00-04)

Core scaffold modules:
- `src/balatroish/cards.py` (cards/deck)
- `src/balatroish/poker.py` (5-card hand evaluator)
- `src/balatroish/scoring.py` (chips × mult scoring model)
- `src/balatroish/round_engine.py` (hand→scoring→reward→shop→progression flow with discards + event log)
- `src/balatroish/sigils.py` (prototype Sigil effects and aggregation)
- `src/balatroish/bosses.py` (prototype boss disruption modifiers)
- `src/balatroish/shop.py` (shop offers and purchasing)
- `src/balatroish/constellation.py` (Constellation Weaving node web + unlock logic)
- `src/balatroish/enhancements.py` (card enhancement framework)
- `src/balatroish/boss_system.py` (boss blueprint categories + telegraph/counterplay)
- `src/balatroish/design_gate.py` (pillar/scope gate checks)
- `src/balatroish/emotion.py` (early/mid/late emotional targeting helper)

Run tests:

```bash
python -m unittest discover -s tests -v
```


## Phase 00-10 Visuals

- Visual doc: `docs/design/visual_00_10.md`
- Runtime helpers: `src/balatroish/visuals.py`

Quick board preview:

```bash
python - <<'PY2'
from src.balatroish.framework import Phase0010Framework
from src.balatroish.visuals import render_terminal_board, visual_snapshot
fw = Phase0010Framework(); fw.bootstrap()
print(render_terminal_board())
print()
print(visual_snapshot(fw))
PY2
```
