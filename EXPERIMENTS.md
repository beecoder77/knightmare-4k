# Tiny Chess — enhancement experiments (19–20 Nov 2026)

Goal: raise the submitted v2 engine (`src2v8.py`, official practice Elo **1809**)
toward the board cap of 2110, spending the last of 3 submissions only on a
candidate proven clearly stronger (gate: ≥ +100 Elo local estimate across
repeated trials plus head-to-head). A new submission replaces v2 entirely,
so a weaker candidate would destroy a certain 1809.

All screening matches: head-to-head vs v8, 12 book openings × both colours,
fixed nodes. Grades: local kit gauntlet (anchors 855…1596, MLE Elo).

| Experiment | Change | Result |
| --- | --- | --- |
| v9 bundle (`src2v9.py`) | reverse futility, LMP, NMP eval-gate, TT depth-preferred, mop-up endgame | 3.5/16 at 20k nodes = **−221 Elo** |
| v9b (v9 minus LMP/RFP) | as above without the two pruning rules | 7.5/16 = **−22 Elo** (parked) |
| Texel tuning (`src2v8t.py`) | 55-param eval fitted to 300k Lichess positions (val loss −4.0%) | 20k match +0; grades below |
| LMR log table (`src2v8L.py`) | R = 0.8 + ln d · ln i / 2.4 | 6.5/16 = **−66 Elo** |
| Passed pawn (`src2v8P.py`) | passed-pawn bonus in the eval file loop | 6.5/16 = **−66 Elo** |

Texel candidate, clean-machine validation (20 Nov, after a contended night
in which the same engines scored 2112 and 0 on different trials — every
"loss" was on time, an artefact of CPU contention, not of the engines):

- Paired grades — trial-0: v8 5.5 (1809) vs v8t 6.0 (2112); trial-1: v8 5.0
  (1654) vs v8t 4.5 (1545); trial-2: v8 4.0 (1451) vs v8t 5.5 (1809).
  Paired differences +0.5 / −0.5 / +1.5 points: inconsistent, inside the
  seed noise of a single engine (v8 alone swings 4.0–5.5).
- Head-to-head at the entry's own budget (95,000 nodes): v8t scored
  4.0/11 (W1 D6 L4) ≈ **−97 Elo** against v8.

**Verdict: NO-GO.** No candidate met the gate; the most regime-relevant
test points negative. The last submission is not spent; v2 (Elo 1809,
already in the final) stands.
