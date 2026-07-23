import subprocess
from subprocess import PIPE
from chess import Move, Board
from enum import IntEnum, StrEnum
from dataclasses import dataclass
from collections import deque


class AnalysisResult(IntEnum):
    percentage = 0
    centipawn_loss = 1
    both = 2


class MoveAnnotation(StrEnum):
    top = "best move"
    good = "good move"
    inaccuracy = "dubious move"
    mistake = "mistake"
    blunder = "blunder"


class AnalysisFeatures:
    fen: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    scores: deque[float] = deque(maxlen=2)
    best_moves: deque[Move] = deque(maxlen=2)
    engine: str = "engines/berserk-14-x86-64.exe"
    depth: int = 12
    result_type: int = AnalysisResult.both
    expanded_annotations: bool = False

    @classmethod
    def change_fen(cls, new_fen: str) -> None:
        if not Board(new_fen).is_valid():
            raise SyntaxError(f"{new_fen} is not a valid fen")
        cls.fen = new_fen


def look_for_line(output: str, target_line: str) -> str:
    """finds target_line in the output, and if such
    is present, returns everything from it and up to the end.
    `print(look_for_line("This chess engine sucks! Stop using it!", "ucks! S"))  # output: ucks! Stop using it!`"""
    subline_at = output.find(target_line)
    if subline_at == -1:
        raise ValueError(f"subline {target_line} wasn't found in output")
    trimmed_line: str = output[subline_at:]
    return trimmed_line


def find_benchmarks(target: str, *benchmarks: str) -> list[str]:
    split_items: list[str] = target.split()
    return [
        split_items[idx + 1]
        for idx in (split_items.index(b) for b in benchmarks)
    ]


@dataclass(init=False)
class MoveAssessment:
    """contains characteristics of an analyzed move"""

    def __init__(self, move: Move) -> None:
        self.move: Move = move  # uci
        self.centipawn_loss: int
        self.best_move: str  # uci
        self.annotation: MoveAnnotation

    def analyze(self, pos: str, engine_process: subprocess.Popen[str]) -> None:
        if engine_process.stdin is None:
            raise ValueError(
                f"bad object {engine_process.stdin} to accept input"
            )

        engine_process.stdin.write(f"position fen {pos}\n")
        output: str
        errors: str
        output, errors = engine_process.communicate(
            input=f"go depth {AnalysisFeatures.depth}\n"
        )
        print(
            find_benchmarks(
                look_for_line(
                    output, f"depth {AnalysisFeatures.depth} seldepth"
                ),
                "depth",
                "bestmove",
                "ponder",
                "nps",
            )
        )


if __name__ == "__main__":
    move_to_evaluate = MoveAssessment(Move.from_uci("b2b3"))
    move_to_evaluate.analyze(
        "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
        subprocess.Popen(
            [AnalysisFeatures.engine],
            stdin=PIPE,
            stdout=PIPE,
            stderr=PIPE,
            text=True,
        ),
    )
