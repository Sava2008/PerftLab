from dataclasses import dataclass
from enum import IntEnum


class TacticType(IntEnum):
    checkmate = 0
    win_material = 1
    avoid_checkmate = 2
    avoid_material_loss = 3


@dataclass
class TacticalPos:
    tactic_type: TacticType
    position: str  # fen string


TACTICAL_POSITIONS: tuple[TacticalPos, ...] = (
    TacticalPos(
        TacticType.checkmate, "8/6k1/Q3bnp1/8/1P6/6KP/1P3r2/6R1 b - - 1 36"
    ),
    TacticalPos(
        TacticType.checkmate,
        "r4rk1/1p2bpp1/4p2R/3pq1N1/2b3R1/8/2P2PPP/q1BQ2K1 w - - 0 28",
    ),
    TacticalPos(
        TacticType.checkmate,
        "R4b1r/4kppp/1N1pb3/4p3/4P3/4BP2/1q4PP/2R3K1 w - - 6 22",
    ),
    TacticalPos(
        TacticType.checkmate,
        "r2qk2r/pp3pp1/3b4/2pp4/4N3/2PBPPp1/PP4P1/R1BQR1K1 b kq - 0 16",
    ),
    TacticalPos(
        TacticType.checkmate,
        "3r2k1/pp4q1/4p1p1/5PQ1/n7/2P2P2/P4P2/1K3B1R b - - 1 25",
    ),
    TacticalPos(
        TacticType.checkmate,
        "4r1qk/pQ2R2p/6p1/3p1r2/P1p5/7P/P2n2PK/8 w - - 1 33",
    ),
    TacticalPos(
        TacticType.checkmate,
        "b4rk1/7p/4p1pP/4PpQ1/2B2P2/4n3/2Pq2P1/1R4K1 w - - 0 25",
    ),
    TacticalPos(
        TacticType.checkmate,
        "1rb2r2/4Bpkn/p1pp4/2b1p3/3nP3/P2P3P/q1PQBP1N/1NK4R w - - 0 21",
    ),
    TacticalPos(
        TacticType.checkmate,
        "4r1qk/pQ2R2p/6p1/3p1r2/P1p5/7P/P2n2PK/8 w - - 1 33",
    ),
)

if __name__ == "__main__":
    print(f"tactical positions: {len(TACTICAL_POSITIONS)}")
