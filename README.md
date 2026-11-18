# knightmare-4k

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/beecoder77/knightmare-4k/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/beecoder77/knightmare-4k/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

Knightmare 4K v2 — a complete chess engine in under 4 KB of Python
(standard library only), built for make.fun's Tiny Chess bounty.
0x88 board, negamax alpha-beta with quiescence, transposition table,
null-move pruning, LMR, killers + history, and a parametric tapered
PeSTO-style evaluation with incremental accumulators, bishop-pair,
pawn-structure and rook-file terms. Deterministic: fixed node budget,
never a clock. Local practice grade: Elo 1809 (v1 was 1451).

`main.py` is the packed entry; it decompresses and runs the engine,
which plays over HTTP against the make.fun environment server
(`POST /game`, then `POST /move {"game": n, "move": "<uci>"}`).

## Run it

```sh
MAKEFUN_ENV_URL=http://127.0.0.1:PORT python3 main.py
```

---
<sub>Entered on [make.fun](https://make.fun/?ref=ws337zp2&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
