import chess
import chess.pgn
import logging
import subprocess


class UCI_command:
    @staticmethod
    def get_best_move(engine, board: chess.Board) -> chess.Move:
        engine.stdin.write("go\n")
        best_move_mark, mv = engine.stdout.flush().readline().split()

        if best_move_mark != "bestmove":
            raise ValueError("wrong uci encoding")

        best_move = chess.Move.from_uci(mv)
        if best_move in board.legal_moves:
            return best_move
        else:
            raise ValueError("illegal move {best_move}")

    @staticmethod
    def has_uci(engine) -> None:
        engine.stdin.write("uci\n")
        if engine.stdin.flush().readline() != "uciok":
            raise ValueError

    @staticmethod
    def check_readiness(engine) -> None:
        engine.stdin.write("ready\n")
        if engine.stdin.flush().readline() != "readyok":
            raise ValueError


def uci_manager(board: chess.Board) -> None:
    white_engine = subprocess.Popen(
        ["Ferrous v0.4.0"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    black_engine = subprocess.Popen(
        ["Ferrous v0.4.0"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    for engine in (white_engine, black_engine):
        UCI_command.has_uci(engine)
        UCI_command.check_readiness(engine)

    while not board.is_game_over():
        match board.turn:
            case chess.WHITE:
                best_move = UCI_command.get_best_move(white_engine, board)
                board.push(best_move)
            case chess.BLACK:
                best_move = UCI_command.get_best_move(black_engine, board)
                board.push(best_move)

    print("quit")
    logging.info(chess.pgn.Game.from_board(board))
    exit(0)
