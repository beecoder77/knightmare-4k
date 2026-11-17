# Knightmare 4K — a tiny chess engine

A complete chess engine in **under 4 KB of Python** (3,457 bytes packed,
standard library only), built for make.fun's *Tiny Chess* bounty: the
strongest engine that fits in 4,096 bytes, playing over HTTP against a
ladder of reference engines.

**Official practice grade: Elo 1451** (server-graded, 2026-11-18) — well
above the 1,154 finalist floor and the ~1,365 house baseline. The field's
practice board later saturated at the 2,110 cap (454 perfect scores), so
the entry stands as a solid, fully working engine rather than a winner.

## What's inside

- `main.py` — the submitted entry: the packed/compressed form of the
  engine (the readable source is `src.py`; the two are kept in sync by
  the make.fun kit's compressor).
- `src.py` — engine v1, readable: 0x88 board representation, negamax
  alpha-beta search, quiescence search (captures + check evasions, delta
  pruning), transposition table, null-move pruning, late-move reductions,
  killer move ordering, tapered piece-square evaluation, pawn-shield king
  safety, and repetition detection via Zobrist hashes seeded into the
  search stack. Deterministic by design: a fixed node budget, never a
  clock.
- `src2.py` — engine v2 (not submitted): parametric PeSTO-style tapered
  evaluation generated from formulas at startup, incremental evaluation
  accumulators, bishop-pair / pawn-structure / rook-file terms, history
  heuristic, futility pruning and adaptive null-move. It beat v1 6–4 in a
  head-to-head match, but not by enough to matter against the saturated
  board, so v1's entry was left standing.

Correctness was established by perft differential testing against
python-chess on the six standard test positions, plus incremental-state
consistency checks over random games.

## Protocol

The engine talks to the make.fun environment server over HTTP:
`POST /game` to start, `POST /move {"game": n, "move": "<uci>"}` to move,
`POST /resign` to resign. It searches from whatever FEN the server deals
(games start from varied openings).

Built by an AI agent (Muse) working for Muhammad Salman Abid.
