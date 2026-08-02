from enum import IntEnum


class PositionAssessment(IntEnum):
    better_for_white = 1
    better_for_black = 2
    equal = 3
    slightly_better_for_white = 4
    slightly_better_for_black = 5
    losing_for_white = 6
    losing_for_black = 7


class OpeningFamily(IntEnum):
    e4 = 1
    d4 = 2
    c4 = 3
    other = 4


class Position:
    def __init__(
        self,
        fen_str: str,
        assessment: PositionAssessment,
        family: OpeningFamily,
        tactical: bool,
    ) -> None:
        self.fen = fen_str
        self.assessment = assessment
        self.family = family or OpeningFamily.other
        self.tactical = tactical or False


# 65 positions for now
STARTING_POSITIONS: tuple[Position, ...] = (
    # Czech defense ❤︎
    Position(
        "rnb1kb1r/pp2pppp/2pp1n2/q7/3PPP2/2N5/PPPB2PP/R2QKBNR b KQkq - 2 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # f4 variation with Bd2
    Position(
        "rnb1kb1r/pp2pppp/2pp1n2/q7/3PPP2/2NB4/PPP3PP/R1BQK1NR b KQkq - 2 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # f4 variation with Bd3
    Position(
        "rnb1kb1r/pp2pppp/2pp1n2/q7/3PPP2/2N5/PPPQ2PP/R1B1KBNR b KQkq - 2 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # f4 variation with Qd2
    Position(
        "rnb1kb1r/pp2pppp/2pp1n2/q3P3/3P1P2/2N5/PPP3PP/R1BQKBNR b KQkq - 0 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # f4 variation with e5
    Position(
        "rn1qkb1r/pp2pppp/2pp1n2/7b/3PP3/2N2N1P/PPP1BPP1/R1BQK2R b KQkq - 2 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        False,
    ),  # Nf3 calm variation
    Position(
        "rn1qkb1r/pp2pppp/2pp1nb1/8/3PP1P1/2NB1N1P/PPP2P2/R1BQK2R b KQkq - 2 7",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        False,
    ),  # Nf3 aggressive variation
    Position(
        "rnbqkb1r/ppp2ppp/3p1n2/3Pp3/4P3/3B4/PPP2PPP/RNBQK1NR b KQkq - 0 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # bishop defense, closed
    Position(
        "rnbqkb1r/ppp2ppp/3p1n2/4p3/3PP3/3B1N2/PPP2PPP/RNBQK2R b KQkq - 1 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # bishop defense with Nf3
    Position(
        "rnbqkb1r/ppp2ppp/5n2/4p3/4P3/3B4/PPP2PPP/RNBQK1NR w KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # bishop defense exchange variation
    Position(
        "rnbqkb1r/ppp2ppp/3p1n2/4p3/3PP3/2PB4/PP3PPP/RNBQK1NR b KQkq - 0 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # bishop defense c3 reinforcement
    # French defense
    Position(
        "r1b1kbnr/pp3ppp/1qn1p3/2ppP3/3P4/P1P2N2/1P3PPP/RNBQKB1R b KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # advance variation main line
    Position(
        "r1b1kbnr/pp3ppp/1qn1p3/2ppP3/3P4/2PB1N2/PP3PPP/RNBQK2R b KQkq - 4 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # advance variation Milner-Barry gambit
    Position(
        "rn1qkbnr/1ppb1ppp/p3p3/3pP3/3P4/5N2/PPP2PPP/RNBQKB1R w KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # advance variation, extended bishop variation
    Position(
        "rnbqkb1r/pp1n1ppp/4p3/2ppP3/3P1P2/2N5/PPP3PP/R1BQKBNR w KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Paulsen variation, classical, Steiniz
    Position(
        "rnbqk2r/ppp1bppp/4pn2/6B1/3PN3/8/PPP2PPP/R2QKBNR w KQkq - 1 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Paulsen variation, classical
    Position(
        "rnb1k2r/ppq1nppp/4p3/2ppP3/3P2Q1/P1P5/2P2PPP/R1B1KBNR w KQkq - 3 8",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Winawer, poisoned pawn variation
    Position(
        "rnbq1rk1/pp2nppp/4p3/2ppP3/3P2Q1/P1P5/2P2PPP/R1B1KBNR w KQ - 3 8",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Winawer, Warsaw variation
    Position(
        "rnbq1k1r/pp2nppp/4p3/2ppP3/3P2Q1/P1P5/2P2PPP/R1B1KBNR w KQ - 3 8",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Winawer, Eingorn variation
    Position(
        "rnbqk2r/pp2nppp/4p3/2ppP3/3P2Q1/P1P5/2P2PPP/R1B1KBNR b KQkq - 1 7",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Winawer variation with Ne7
    Position(
        "rnbqkb1r/pp1n1ppp/4p3/2ppP3/3P4/2PB4/PP1N1PPP/R1BQK1NR b KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # closed Tarrash variation
    Position(
        "rnbqkb1r/pp3ppp/5n2/2pp4/3P4/5N2/PPPN1PPP/R1BQKB1R w KQkq - 2 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # open Tarrash variation, old main line
    Position(
        "r1bqkbnr/pp3ppp/2n1p3/2pp4/3PP3/5N2/PPPN1PPP/R1BQKB1R w KQkq - 2 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Tarrash variation, open system with Nc6
    Position(
        "rnbqkbnr/pp3ppp/4p3/3p4/3pP3/5N2/PPPN1PPP/R1BQKB1R w KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Tarrash variation, open system with cxd4
    Position(
        "rnbqk2r/ppp1bppp/5n2/3p4/3P4/3B1N2/PPP2PPP/RNBQK2R w KQkq - 4 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        False,
    ),  # exchange variation
    # Caro-Kann defense
    Position(
        "rn1qkbnr/pp2ppp1/2p5/3pPb1p/3P3P/8/PPP2PP1/RNBQKBNR w KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Tal variation with h5
    Position(
        "rn2kbnr/pp2pppp/1qp5/3pPb2/3P3P/8/PPP2PP1/RNBQKBNR w KQkq - 1 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Tal variation with Qb6
    Position(
        "rn1qkbnr/pp3ppp/2p1p3/3pPb2/3P4/5N2/PPP1BPPP/RNBQK2R b KQkq - 1 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Short variation with Be2
    Position(
        "rn1qkbnr/pp3ppp/2p1p3/3pPb2/3P4/2P2N2/PP3PPP/RNBQKB1R b KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Short variation with c3
    Position(
        "rn1qkbnr/pp3ppp/2p1p3/3pPb2/3P4/P4N2/1PP2PPP/RNBQKB1R b KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Short variation with a3!?
    Position(
        "rn1qkbnr/pp3ppp/4p1b1/2ppP3/3P2P1/2N5/PPP1NP1P/R1BQKB1R w KQkq - 0 7",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Van der Wiel attack
    Position(
        "rn1qkbnr/pp3ppp/2p1p3/3pP3/3P4/2PQ4/PP3PPP/RNB1K1NR b KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, immediate c3
    Position(
        "rnbqkbnr/pp3ppp/4p3/2PpP3/8/4B3/PPP2PPP/RN1QKBNR b KQkq - 1 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Botvinnik-Carls defense with dxc5 and Be3
    Position(
        "rnbqkbnr/pp3ppp/4p3/2PpP3/8/P7/1PP2PPP/RNBQKBNR b KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Botvinnik-Carls defense with dxc5 and a3
    Position(
        "r2qkbnr/pp2pppp/2n5/3pP3/3P2b1/5N2/PP3PPP/RNBQKB1R w KQkq - 1 7",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Botvinnik-Carls defense with c3
    Position(
        "r2qkbnr/pp2pppp/2n5/3pPb2/3P4/2N5/PP3PPP/R1BQKBNR w KQkq - 3 7",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # advance, Botvinnik-Carls defense with early cxd4
    Position(
        "r1bqkbnr/pp2pppp/2n5/3p4/3P4/3B4/PPP2PPP/RNBQK1NR w KQkq - 2 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # exchange variation
    Position(
        "rnb1kbnr/pp3ppp/1qp5/8/3pP3/2N2N2/PPP3PP/R1BQKB1R w KQkq - 0 7",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Fantasy variation, best line
    Position(
        "r1bqk1nr/pp1n1ppp/2p1p3/3p4/1b1PP3/2N1BP2/PPP3PP/R2QKBNR w KQkq - 4 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Fantasy variation, French variation
    Position(
        "rnbqk1nr/pp3ppp/2p1p3/3p4/3PP3/P1P2P2/2P3PP/R1BQKBNR b KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Fantasy variation, French variation with Bb4
    Position(
        "rn1qkbnr/pp3ppp/2p5/4p3/3PP1b1/2P2N2/PP4PP/RNBQKB1R b KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Fantasy variation, classical
    # open Sicilian defense
    Position(
        "rnbqkb1r/1p2pppp/p2p1n2/6B1/3NP3/2N5/PPP2PPP/R2QKB1R b KQkq - 1 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Najdorf with Bg5
    Position(
        "rnbqkb1r/1p2pppp/p2p1n2/8/3NP3/2N1B3/PPP2PPP/R2QKB1R b KQkq - 1 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Najdorf, English attack
    Position(
        "rnbqkb1r/1p2pppp/p2p1n2/8/2BNP3/2N5/PPP2PPP/R1BQK2R b KQkq - 1 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Najdorf, Fischer-Sozin attack
    Position(
        "rnbqkb1r/pp2pp1p/3p1np1/8/3NPP2/2N5/PPP3PP/R1BQKB1R b KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Dragon, Levenfish variation
    Position(
        "rnbqk2r/pp2ppbp/3p1np1/8/3NP3/2N1BP2/PPP3PP/R2QKB1R b KQkq - 0 7",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Dragon, Yugoslav attack
    Position(
        "rnbqk2r/pp2ppbp/3p1np1/8/3NP3/2N3P1/PPP2PBP/R1BQK2R b KQkq - 2 7",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Dragon, Fianchetto variation
    Position(
        "rnbqk2r/pp2ppbp/3p1np1/8/3NP3/2N1B3/PPP1BPPP/R2QK2R b KQkq - 3 7",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Dragon, classical variation
    Position(
        "rnbqkb1r/pp3ppp/3ppn2/8/3NP1P1/2N5/PPP2P1P/R1BQKB1R b KQkq - 0 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Sheveningen, Keres attack
    Position(
        "rnbqkb1r/1p3ppp/p2ppn2/8/3NP3/2N1B3/PPP2PPP/R2QKB1R w KQkq - 0 7",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Sheveningen, Najdorf hybrid
    # closed Sicilian defense
    Position(
        "r1bqk1nr/pp1pppbp/2n3p1/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq - 1 6",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # Chameleon
    Position(
        "r1bqkb1r/pp2pppp/2n5/2pn4/8/2NP2P1/PPP2P1P/R1BQKBNR w KQkq - 0 6",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.e4,
        True,
    ),  # d3 variation
    Position(
        "r1bqk1nr/pp1pppbp/2n3p1/2p5/4P3/2N3P1/PPPP1PBP/R1BQK1NR w KQkq - 2 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # classical closed
    # Alapin Sicilian
    Position(
        "rnbqkb1r/pp1ppppp/8/3nP3/3p4/2P5/PP3PPP/RNBQKBNR w KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Nf6, d5 - Nd5, d4
    Position(
        "rnbqkb1r/pp1ppppp/8/2pnP3/8/2P2N2/PP1P1PPP/RNBQKB1R b KQkq - 2 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Nf3
    Position(
        "rnb1kb1r/pp2pppp/5n2/2pq4/3P4/2P5/PP3PPP/RNBQKBNR w KQkq - 1 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # 2. d5
    # Vienna game
    Position(
        "rnbqkb1r/pppp1ppp/5n2/4p3/4PP2/2N5/PPPP2PP/R1BQKBNR b KQkq - 0 3",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Vienna gambit
    Position(
        "r1bqkb1r/pppp1ppp/5n2/n3p3/2B1P3/2NP4/PPP2PPP/R1BQK1NR w KQkq - 1 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # 2. Nc6
    Position(
        "r1b1k1nr/pppp1ppp/2n2q2/2b1p3/2B1P1Q1/2N5/PPPP1PPP/R1B1K1NR w KQkq - 6 5",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        True,
    ),  # copycat with Qf6
    # Danish gambit
    Position(
        "rnbqk1nr/pppp1ppp/8/2b5/4P3/2N5/PP3PPP/R1BQKBNR w KQkq - 1 5",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.e4,
        True,
    ),  # Single Danish
    Position(
        "rnbqkbnr/pppp1ppp/8/8/2B1P3/8/PB3PPP/RN1QK1NR b KQkq - 0 5",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.e4,
        True,
    ),  # Double Danish
    Position(
        "rnbqk1nr/pppp1ppp/8/8/1bB1P3/8/PB3PPP/RN1QK1NR w KQkq - 1 6",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.e4,
        True,
    ),  # Copengagen defense
    # Owen's defense
    Position(
        "rn1qkb1r/pbpp1ppp/1p2pn2/8/3PP3/3B1N2/PPP2PPP/RNBQK2R w KQkq - 2 5",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        False,
    ),  # 3. Bd3
    Position(
        "rn1qk1nr/pbpp1ppp/1p2p3/8/1b1PP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq - 2 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        False,
    ),  # 3. Nc3?!
    Position(
        "rn1qk1nr/pbpp1ppp/1p2p3/8/1bPPP3/3B4/PP3PPP/RNBQK1NR w KQkq - 1 5",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.e4,
        False,
    ),  # included c4 move
    # modern defense
    Position(
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP3/2N2N2/PPP2PPP/R1BQKB1R w KQkq - 2 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # 3. Bd3
    Position(
        "rnbqk1nr/ppppppbp/6p1/8/3PP2P/8/PPP2PP1/RNBQKBNR b KQkq - 0 3",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Fischer's attack
    Position(
        "rnbqk1nr/1pp1ppbp/p2p2p1/8/3PP3/2N1B3/PPP2PPP/R2QKBNR w KQkq - 0 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),
    # Scotch opening
    Position(
        "r1bqkbnr/pppp1ppp/2n5/8/3pP3/2P2N2/PP3PPP/RNBQKB1R b KQkq - 0 4",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.e4,
        True,
    ),  # Göring gambit
    Position(
        "r1bqkbnr/pppp1ppp/2n5/8/2BpP3/5N2/PPP2PPP/RNBQK2R b KQkq - 1 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Scotch gambit
    Position(
        "r1bqkbnr/pppp1ppp/2n5/8/3NP3/8/PPP2PPP/RNBQKB1R b KQkq - 0 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # normal Scotch game
    # Italian game
    Position(
        "r1bqkb1r/pppp1ppp/2n2n2/4p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # two knights defense
    Position(
        "r1bqk1nr/pppp1ppp/2n5/2b1p3/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 4 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # Giuoco piano
    Position(
        "r1bqk1nr/pppp1ppp/2n5/2b1p3/1PB1P3/5N2/P1PP1PPP/RNBQK2R b KQkq - 0 4",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.e4,
        True,
    ),  # Evans' gambit
    # Ruy Lopez
    Position(
        "r1bqk2r/pppp1ppp/2n2n2/1Bb1p3/4P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 1 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Berlin defense with immediate d3
    Position(
        "r1bqkb1r/pppp1ppp/2n2n2/1B2p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 b kq - 5 4",
        PositionAssessment.equal,
        OpeningFamily.e4,
        True,
    ),  # Berlin defense, Rio gambit
    Position(
        "r1bqkbnr/1pp2ppp/p1p5/4p3/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # Morphy defense, exchange variation
    Position(
        "r1bqkb1r/1ppp1ppp/p1n2n2/4p3/B3P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 2 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # Morphy defense, closed variation
    Position(
        "r1bqk2r/pppp1ppp/2n2n2/1Bb1p3/4P3/2P2N2/PP1P1PPP/RNBQK2R w KQkq - 1 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # classical defense, central variation
    Position(
        "r1bqk2r/pppp1ppp/2n2n2/1Bb1p3/4P3/5N2/PPPP1PPP/RNBQ1RK1 w kq - 6 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # classical defense, Beverwijk variation
    # Philidor defense
    Position(
        "r1bqkbnr/pp1n1ppp/2pp4/4p3/2BPP3/5N2/PPP2PPP/RNBQK2R w KQkq - 0 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        False,
    ),  # Hanham variation
    Position(
        "rnbqk2r/ppp1bppp/3p1n2/8/3NP3/2N5/PPP2PPP/R1BQKB1R w KQkq - 3 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        False,
    ),  # Exchange variation
    Position(
        "rnbqk2r/ppp1bppp/3p1n2/4p3/2B1P3/3P1N2/PPP2PPP/RNBQK2R w KQkq - 1 5",
        PositionAssessment.equal,
        OpeningFamily.e4,
        False,
    ),  # Italian-like system
    # queen's gambit declined
    Position(
        "rnbqk2r/ppp1bppp/4pn2/3p2B1/2PP4/2N5/PP2PPPP/R2QKBNR w KQkq - 4 5",
        PositionAssessment.equal,
        OpeningFamily.d4,
        True,
    ),  # Orthodox variation
    Position(
        "rnbq1rk1/ppp1bppp/4pn2/3p4/2PP1B2/2N1P3/PP3PPP/R2QKBNR w KQ - 1 6",
        PositionAssessment.equal,
        OpeningFamily.d4,
        True,
    ),  # Harrwitz variation
    Position(
        "rnbqk1nr/pp3ppp/2p1p3/8/PbpP4/2N1PN2/1P3PPP/R1BQKB1R b KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.d4,
        True,
    ),  # Noteboom variation
    # queen's gambit accepted
    Position(
        "r2qkbnr/ppp2ppp/2n1b3/8/2BpP3/5N2/PP3PPP/RNBQ1RK1 w kq - 3 7",
        PositionAssessment.equal,
        OpeningFamily.d4,
        False,
    ),  # McDonnel defense
    Position(
        "rnbqkb1r/1p3ppp/p3pn2/2p5/2BP4/4PN2/PP3PPP/RNBQ1RK1 w kq - 0 7",
        PositionAssessment.equal,
        OpeningFamily.d4,
        False,
    ),  # classical defense, main line
    Position(
        "rnbqkb1r/1p3ppp/p3pn2/2p5/2BP4/4PN2/PP3PPP/RNBQ1RK1 w kq - 0 7",
        PositionAssessment.equal,
        OpeningFamily.d4,
        False,
    ),  # 3. e3
    # Nimzo Indian defense
    Position(
        "rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR w KQ - 4 5",
        PositionAssessment.equal,
        OpeningFamily.d4,
        True,
    ),  # classical Nimzo Indian
    Position(
        "rnb1k2r/ppppqppp/4pn2/8/1bPP4/5N2/PP1BPPPP/RN1QKB1R w KQkq - 4 5",
        PositionAssessment.equal,
        OpeningFamily.d4,
        True,
    ),  # Bogo-Indian defense, Nimzowitsch variation
    Position(
        "rnbqk2r/p1pp1ppp/1p2pn2/8/1bPP4/5N2/PP1NPPPP/R1BQKB1R w KQkq - 0 5",
        PositionAssessment.equal,
        OpeningFamily.d4,
        True,
    ),  # Bogo-Indian defense, Grünfeld variation
    Position(
        "rnbqk2r/p1pp1ppp/1p2pn2/8/1bPP4/2N1P3/PP2NPPP/R1BQKB1R b KQkq - 1 5",
        PositionAssessment.equal,
        OpeningFamily.d4,
        True,
    ),  # Rubenstein system
    Position(
        "rnbqk2r/pppp1ppp/4pn2/6B1/1bPP4/2N5/PP2PPPP/R2QKBNR b KQkq - 3 4",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.d4,
        True,
    ),  # Leningrad variation
    # Benoni defense
    Position(
        "rnbqk2r/pp3pbp/3p1np1/2pP4/4P3/2N2N2/PP3PPP/R1BQKB1R w KQkq - 2 8",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.d4,
        True,
    ),  # modern Benoni
    Position(
        "rnbqkb1r/3ppppp/p4n2/1PpP4/8/8/PP2PPPP/RNBQKBNR w KQkq - 0 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.d4,
        True,
    ),  # Benko gambit
    Position(
        "rnbqk2r/pp2ppbp/3p1np1/2pP4/2P1P3/2NB4/PP3PPP/R1BQK1NR b KQkq - 2 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.d4,
        True,
    ),  # old Benoni
    # Dutch defense
    Position(
        "rnbqk2r/ppp1p1bp/3p1np1/5p2/2PP4/2N2NP1/PP2PP1P/R1BQKB1R w KQkq - 0 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.d4,
        True,
    ),  # queen's knight variation
    Position(
        "rnbqkb1r/pp4pp/2p1pn2/3p1p2/2PP4/5NP1/PP2PPBP/RNBQK2R w KQkq - 0 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.d4,
        True,
    ),  # stonewall Dutch
    Position(
        "rnbqkb1r/ppp1p2p/5np1/3p2B1/3Pp2P/2N5/PPP2PP1/R2QKBNR w KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.d4,
        True,
    ),  # Staunton gambit
    # Larsen attack
    Position(
        "r1bqk1nr/ppp2ppp/2nb4/1B1pp3/8/1P2P3/PBPP1PPP/RN1QK1NR w KQkq - 2 5",
        PositionAssessment.equal,
        OpeningFamily.other,
        True,
    ),  # modern variation
    Position(
        "r1b1kb1r/pp2pppp/1qn2n2/1Bpp4/2P5/1P2PN2/PB1P1PPP/RN1QK2R b KQkq - 0 6",
        PositionAssessment.equal,
        OpeningFamily.other,
        True,
    ),  # delayed e5
    Position(
        "rn1qkb1r/ppp2pp1/4pn1p/3p1b2/8/1P2PN2/PBPPBPPP/RN1QK2R w KQkq - 0 6",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.other,
        True,
    ),  # classical variation
    # Pirc defense
    Position(
        "rnbqk2r/pp2ppbp/3p1np1/2p5/3PPP2/2N2N2/PPP3PP/R1BQKB1R w KQkq - 0 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Austrian attack, dragon formation
    Position(
        "rnbqk2r/pp2ppbp/2pp1np1/8/3PPP2/2N2N2/PPP3PP/R1BQKB1R w KQkq - 0 6",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Austrian attack, Czech structure
    Position(
        "rnbq1rk1/pp2ppbp/2pp1np1/8/3PP3/2N2N2/PPP1BPPP/R1BQ1RK1 w - - 0 7",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # classical
    Position(
        "rnbqk2r/ppp1ppbp/3p1np1/6B1/3PP3/2N5/PPP2PPP/R2QKBNR w KQkq - 2 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Byrne attack
    Position(
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP3/2N1BN2/PPP2PPP/R2QKB1R b KQkq - 3 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # 150 attack
    Position(
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP1P1/2N5/PPP1BP1P/R1BQK1NR b KQkq - 0 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Chinese attack
    Position(
        "rnbqk2r/ppp1ppbp/3p1np1/8/3PP1P1/2N5/PPP1BP1P/R1BQK1NR b KQkq - 0 5",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Chinese attack
    # weird gambits
    Position(
        "rnbqkbnr/ppp1pppp/8/3p4/3PP3/8/PPP2PPP/RNBQKBNR b KQkq - 0 2",
        PositionAssessment.slightly_better_for_black,
        OpeningFamily.d4,
        True,
    ),  # Blackmar Diemer gambit
    Position(
        "rnbqk1nr/ppp2ppp/3b4/8/8/8/PPP1PPPP/RNBQKBNR w KQkq - 0 4",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.d4,
        False,
    ),  # Englund gambit
    Position(
        "rnbqkb1r/pppppppp/5n2/8/3PP3/8/PPP2PPP/RNBQKBNR b KQkq - 0 2",
        PositionAssessment.better_for_black,
        OpeningFamily.d4,
        False,
    ),  # Omega gambit
    Position(
        "rnbqkbnr/ppp2ppp/8/3pp3/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3",
        PositionAssessment.slightly_better_for_white,
        OpeningFamily.e4,
        True,
    ),  # elephant gambit
    Position(
        "rnbqkbnr/pppp2pp/8/4pp2/4P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 0 3",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Latvian gambit
    Position(
        "r1bqkbnr/pppp2pp/2n5/4pp2/2B1P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 4",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Rousseau gambit
    Position(
        "r1bqkbnr/pppp2pp/2n5/1B2pp2/4P3/5N2/PPPP1PPP/RNBQK2R w KQkq - 0 4",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Jaenish gambit
    Position(
        "rnbqkbnr/ppppp1pp/8/5p2/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Duras gambit
    Position(
        "rnbqkbnr/pp2pppp/2p5/3P4/8/8/PPPP1PPP/RNBQKBNR w KQkq - 0 3",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Blackburne-Kloosterboer gambit
    Position(
        "rn1qkb1r/ppp1pppp/5n2/3P4/3P2b1/8/PPP2PPP/RNBQKBNR w KQkq - 1 4",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        True,
    ),  # Portuguese gambit
    Position(
        "rnbqkbnr/pppp1ppp/8/4p3/4PP2/8/PPPP2PP/RNBQKBNR b KQkq - 0 2",
        PositionAssessment.better_for_white,
        OpeningFamily.e4,
        True,
    ),  # King's gambit
)

if __name__ == "__main__":
    print(f"positions: {len(STARTING_POSITIONS)}")
