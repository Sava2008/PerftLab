import chess_analysis

TEST_SUBJECTS: tuple[str, ...] = (
    """info string Available processors: 0-3
info string Using 1 thread
info string NNUE evaluation using nn-c288c895ea92.nnue (125MiB, (102384, 1024, 15, 32, 1))
info string NNUE evaluation using nn-37f18f62d772.nnue (6MiB, (22528, 128, 15, 32, 1))
info string Network replica 1: Shared memory.
info depth 1 seldepth 4 multipv 1 score cp -3 nodes 55 nps 3928 hashfull 0 tbhits 0 time 14 pv f1e2
info depth 2 seldepth 4 multipv 1 score cp 0 nodes 101 nps 6312 hashfull 0 tbhits 0 time 16 pv f1e2
info depth 3 seldepth 4 multipv 1 score cp 4 nodes 171 nps 9000 hashfull 0 tbhits 0 time 19 pv f1e2
info depth 4 seldepth 8 multipv 1 score cp 9 nodes 251 nps 11952 hashfull 0 tbhits 0 time 21 pv f1e2
info depth 5 seldepth 8 multipv 1 score cp 32 nodes 436 nps 18166 hashfull 0 tbhits 0 time 24 pv f1e2
info depth 6 seldepth 9 multipv 1 score cp 31 nodes 631 nps 22535 hashfull 0 tbhits 0 time 28 pv f1e2 a7a6 a2a4
info depth 7 seldepth 8 multipv 1 score cp 46 nodes 1211 nps 31051 hashfull 0 tbhits 0 time 39 pv f1e2 a7a6
info depth 8 seldepth 11 multipv 1 score cp 45 nodes 5099 nps 57943 hashfull 2 tbhits 0 time 88 pv a2a3 g8h6 b2b4 c5d4 c1h6 g7h6 c3d4 a7a5
info depth 9 seldepth 11 multipv 1 score cp 45 nodes 7000 nps 61946 hashfull 3 tbhits 0 time 113 pv a2a3 g8h6 b2b4 c5d4 c1h6 g7h6 c3d4 a7a5
info depth 10 seldepth 18 multipv 1 score cp 58 nodes 15044 nps 76365 hashfull 5 tbhits 0 time 197 pv a2a3 a7a5 f1d3 c8d7 d4c5 f8c5 e1g1 g8e7
info depth 11 seldepth 21 multipv 1 score cp 43 nodes 39708 nps 86134 hashfull 13 tbhits 0 time 461 pv a2a3 c5c4 b1d2 c8d7 b2b3 c4b3 d2b3 c6a5 b3a5 b6a5
info depth 12 seldepth 19 multipv 1 score cp 41 nodes 43716 nps 86395 hashfull 14 tbhits 0 time 506 pv a2a3 a7a5 f1d3 c8d7 d3c2 b6a6 b2b3 c5d4 c3d4 a8c8 b1c3
bestmove a2a3 ponder a7a5""",
    """info string Available processors: 0-3
info string Using 1 thread
info string NNUE evaluation using nn-c288c895ea92.nnue (125MiB, (102384, 1024, 15, 32, 1))
info string NNUE evaluation using nn-37f18f62d772.nnue (6MiB, (22528, 128, 15, 32, 1))
info string Network replica 1: Shared memory.
info depth 1 seldepth 2 multipv 1 score cp -30 nodes 3 nps 250 hashfull 0 tbhits 0 time 12 pv e1f1
info depth 2 seldepth 3 multipv 1 score cp 22 nodes 11 nps 785 hashfull 0 tbhits 0 time 14 pv e1f1
info depth 3 seldepth 5 multipv 1 score cp 41 nodes 35 nps 2058 hashfull 0 tbhits 0 time 17 pv e1f1
info depth 4 seldepth 7 multipv 1 score cp -12 nodes 227 nps 11350 hashfull 0 tbhits 0 time 20 pv e1f1 a8c8
info depth 5 seldepth 7 multipv 1 score cp -31 nodes 337 nps 15318 hashfull 0 tbhits 0 time 22 pv e1f1 a8c8 g2g3 c8c5 d4c5
info depth 6 seldepth 8 multipv 1 score cp -26 nodes 625 nps 22321 hashfull 0 tbhits 0 time 28 pv e1f1 d7c6 g2g3 b7b6 c5a6
info depth 7 seldepth 9 multipv 1 score cp -40 nodes 1184 nps 32888 hashfull 0 tbhits 0 time 36 pv e1f1 a8c8 c5d7 e8d7 g2g3 d7e7 a1b1
info depth 8 seldepth 18 multipv 1 score cp -22 nodes 5651 nps 63494 hashfull 2 tbhits 0 time 89 pv e1f1 d7c6 a1c1 c3a3 c1a1 a3c3 a1c1 c3b2
info depth 9 seldepth 10 multipv 1 score cp -1 nodes 6798 nps 66000 hashfull 2 tbhits 0 time 103 pv e1f1 d7c6 a1c1 c3a3
info depth 10 seldepth 13 multipv 1 score cp -1 nodes 7924 nps 68904 hashfull 2 tbhits 0 time 115 pv e1f1 d7c6 a1c1 c3a3 c1a1 a3c3 a1c1 c3b2
info depth 11 seldepth 10 multipv 1 score cp 0 nodes 8049 nps 68211 hashfull 2 tbhits 0 time 118 pv e1f1 d7c6 a1c1 c3a3 c1a1 a3c3 a1c1 c3a3
info depth 12 seldepth 8 multipv 1 score cp 0 nodes 8335 nps 68319 hashfull 3 tbhits 0 time 122 pv e1f1 d7c6 a1c1 c3a3 c1a1 a3c3 a1c1
bestmove e1f1 ponder d7c6""",
    """info string Available processors: 0-3
info string Using 1 thread
info string NNUE evaluation using nn-c288c895ea92.nnue (125MiB, (102384, 1024, 15, 32, 1))
info string NNUE evaluation using nn-37f18f62d772.nnue (6MiB, (22528, 128, 15, 32, 1))
info string Network replica 1: Shared memory.
info depth 1 seldepth 5 multipv 1 score cp -405 nodes 58 nps 292 hashfull 0 tbhits 0 time 198 pv c8c2 e3g4
info depth 2 seldepth 4 multipv 1 score cp -405 nodes 106 nps 532 hashfull 0 tbhits 0 time 199 pv c8c2 e3g4
info depth 3 seldepth 5 multipv 1 score cp -449 nodes 155 nps 775 hashfull 0 tbhits 0 time 200 pv c8c2 e3g4 c2c1 a1c1
info depth 4 seldepth 5 multipv 1 score cp -449 nodes 212 nps 1049 hashfull 0 tbhits 0 time 202 pv c8c2 e3g4 c2c1 a1c1
info depth 5 seldepth 6 multipv 1 score cp -466 nodes 277 nps 1357 hashfull 0 tbhits 0 time 204 pv g4e4 c2e4 c8c1 a1c1
info depth 6 seldepth 8 multipv 1 score cp -483 nodes 382 nps 1854 hashfull 0 tbhits 0 time 206 pv c8c2 e3g4 c2d2 c1c8 g7f8
info depth 7 seldepth 8 multipv 1 score cp -484 nodes 507 nps 2437 hashfull 0 tbhits 0 time 208 pv g4e4 c2e4 c8c1 a1c1 d5e4
info depth 8 seldepth 11 multipv 1 score cp -486 nodes 640 nps 3047 hashfull 0 tbhits 0 time 210 pv c8c2 e3g4 c2c1 a1c1 g8f8 c1c8 f8e7
info depth 9 seldepth 11 multipv 1 score cp -501 nodes 835 nps 3920 hashfull 0 tbhits 0 time 213 pv c8c2 e3g4 c2c1 a1c1 g8f8 g2h1 f8e8
info depth 10 seldepth 14 multipv 1 score cp -558 nodes 1947 nps 8931 hashfull 0 tbhits 0 time 218 pv c8c2 e3g4 c2c1 a1c1 g8f8 g4e3 f8g8 g2h1
info depth 11 seldepth 16 multipv 1 score cp -564 nodes 3523 nps 15588 hashfull 1 tbhits 0 time 226 pv c8c2 e3g4 c2c4 g4f6 g8f8 f6h5 f8g8 h5g7 g8g7
info depth 12 seldepth 17 multipv 1 score cp -558 nodes 5330 nps 22680 hashfull 1 tbhits 0 time 235 pv c8c2 e3g4 c2c4 g2h1 h6h5 g4e3 c4c1 a1c1 g7h6 c1c8 g8g7
bestmove c8c2 ponder e3g4""",
)

ANSWERS: tuple[list[str], ...] = (
    ["12", "19", "86395", "506", "a2a3"],
    ["12", "8", "68319", "122", "e1f1"],
    ["12", "17", "22680", "235", "c8c2"],
)


def find_benchmark_test() -> None:
    targets: tuple[str, ...] = "depth", "seldepth", "nps", "time", "bestmove"
    for output, answer in zip(TEST_SUBJECTS, ANSWERS):
        assert answer == chess_analysis.find_benchmarks(
            chess_analysis.look_for_line(output, "depth 12 seldepth"), *targets
        )


find_benchmark_test()
