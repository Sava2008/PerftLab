import chess
import chess.pgn
import logging
from datetime import date


class UCI_command:
    @staticmethod
    def get_best_move(engine, board: chess.Board) -> chess.Move:
        engine.stdin.write(f"position fen {board.fen()}\n")
        engine.stdin.write("go\n")
        engine.stdin.flush()
        best_move_mark, mv = engine.stdout.readline().strip().split()

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
        engine.stdin.flush()

        if engine.stdout.readline().strip() != "uciok":
            raise ValueError

    @staticmethod
    def check_readiness(engine) -> None:
        engine.stdin.write("isready\n")
        engine.stdin.flush()

        if engine.stdout.readline().strip() != "readyok":
            raise ValueError

    @staticmethod
    def start_new_game(engine) -> None:
        engine.stdin.write("ucinewgame\n")
        engine.stdin.flush()


def uci_manager(
    board: chess.Board,
    white_engine,
    black_engine,
    white_engine_path: str,
    black_engine_path: str,
) -> None:
    for engine in (white_engine, black_engine):
        UCI_command.start_new_game(engine)
        UCI_command.check_readiness(engine)

    while not board.is_game_over():
        match board.turn:
            case chess.WHITE:
                best_move = UCI_command.get_best_move(white_engine, board)
                board.push(best_move)
            case chess.BLACK:
                best_move = UCI_command.get_best_move(black_engine, board)
                board.push(best_move)

    game_pgn = chess.pgn.Game.from_board(board)
    game_pgn.headers["White"] = white_engine_path.removesuffix(".exe")
    game_pgn.headers["Black"] = black_engine_path.removesuffix(".exe")
    game_pgn.headers["TimeControl"] = "60+0"
    game_pgn.headers["Site"] = "PerftLab"
    game_pgn.headers["Round"] = "-"
    game_pgn.headers["WhiteElo"] = "1850"
    game_pgn.headers["BlackElo"] = "1850"
    game_pgn.headers["Date"] = f"{date.today().strftime('%Y.%m.%d')}"
    logging.info(game_pgn)
