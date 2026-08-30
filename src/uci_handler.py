import logging
from datetime import date
from time import time

import chess
import chess.pgn
from chess import Move

from time_control import TimeControl


class UCI_command:
    @staticmethod
    def get_best_move(engine, board: chess.Board, movetime_ms: int) -> Move:
        assert engine.poll() is None
        engine.stdin.write(f"position fen {board.fen()}\n")
        engine.stdin.write(f"go movetime {movetime_ms}\n")
        engine.stdin.flush()
        while True:
            line = engine.stdout.readline()
            if not line:
                raise RuntimeError(engine.stderr.read())
            elif not line.startswith("bestmove "):
                continue
            mv = line.strip().split()[1]

            best_move = chess.Move.from_uci(mv)
            if best_move in board.legal_moves:
                return best_move
            else:
                raise ValueError(f"illegal move {best_move}, on board {board}")

    @staticmethod
    def has_uci(engine) -> None:
        engine.stdin.write("uci\n")

        engine.stdin.flush()

        while True:
            line = engine.stdout.readline()

            if not line:
                raise RuntimeError(engine.stderr.read())

            line = line.strip()

            if line == "uciok":
                return

    @staticmethod
    def check_readiness(engine) -> None:
        engine.stdin.write("isready\n")
        engine.stdin.flush()

        while True:
            line = engine.stdout.readline().strip()
            if not line:
                raise RuntimeError(engine.stderr.read())

            line = line.strip()
            
            if line == "readyok":
                return

    @staticmethod
    def start_new_game(engine) -> None:
        engine.stdin.write("ucinewgame\n")
        engine.stdin.flush()


def conclude_game(
    game_pgn,
    result: str | None,
    white_player: str,
    black_player: str,
    time_control: str,
    white_elo: int,
    black_elo: int,
) -> None:
    game_pgn.headers["White"] = white_player
    game_pgn.headers["Black"] = black_player
    game_pgn.headers["TimeControl"] = time_control
    game_pgn.headers["Site"] = "PerftLab"
    game_pgn.headers["Round"] = "-"
    game_pgn.headers["WhiteElo"] = str(white_elo)
    game_pgn.headers["BlackElo"] = str(black_elo)
    game_pgn.headers["Date"] = f"{date.today().strftime('%Y.%m.%d')}"

    if result is not None:
        game_pgn.headers["Result"] = result

    logging.info(game_pgn)


def conclude_game_timeout(
    board,
    white_engine_path: str,
    black_engine_path,
    side_time_control: TimeControl,
    side: chess.Color,
) -> str:
    enemy_color: chess.Color = (
        chess.BLACK if side == chess.WHITE else chess.WHITE
    )
    result: str
    game_pgn = chess.pgn.Game.from_board(board)
    if board.has_insufficient_material(enemy_color):
        result = "1/2-1/2"
        conclude_game(
            game_pgn,
            "1/2-1/2",
            white_engine_path,
            black_engine_path,
            side_time_control.convert_to_pgn_time(),
            1850,
            1850,
        )
    else:
        result = "0-1" if side == chess.WHITE else "1-0"
        conclude_game(
            game_pgn,
            result,
            white_engine_path,
            black_engine_path,
            side_time_control.convert_to_pgn_time(),
            1850,
            1850,
        )
    return result


def claim_winner(
    game_result: str,
    white_engine_path: str,
    black_engine_path: str,
    engine1_path: str,
    engine2_path: str,
) -> tuple[int, int]:

    winner_path = None
    if game_result == "1-0":
        winner_path = white_engine_path
    elif game_result == "0-1":
        winner_path = black_engine_path

    if winner_path == engine1_path:
        return (1, 0)
    elif winner_path == engine2_path:
        return (0, 1)
    return (0, 0)


def uci_manager(
    board: chess.Board,
    white_engine,
    black_engine,
    white_engine_path: str,
    black_engine_path: str,
    engine1_path: str,
    engine2_path: str,
    engine1_score: int,
    engine2_score: int,
) -> tuple[int, int]:
    for engine in (white_engine, black_engine):
        UCI_command.start_new_game(engine)
        UCI_command.check_readiness(engine)

    white_time_control = TimeControl(0, 1, 0, 0)
    black_time_control = TimeControl(0, 1, 0, 0)
    mutual_movetime: int = 500
    while not board.is_game_over():
        game_result: str
        match board.turn:
            case chess.WHITE:
                if white_time_control.time_as_secs <= 0:
                    game_result = conclude_game_timeout(
                        board,
                        white_engine_path,
                        black_engine_path,
                        white_time_control,
                        chess.WHITE,
                    )
                    return claim_winner(
                        game_result,
                        white_engine_path,
                        black_engine_path,
                        engine1_path,
                        engine2_path,
                    )
                start = time()
                best_move = UCI_command.get_best_move(
                    white_engine, board, mutual_movetime
                )
                board.push(best_move)
                end = time()
                white_time_control.decrease_time(end - start)
                if white_time_control.time_as_secs <= 0:
                    game_result = conclude_game_timeout(
                        board,
                        white_engine_path,
                        black_engine_path,
                        white_time_control,
                        chess.WHITE,
                    )
                    return claim_winner(
                        game_result,
                        white_engine_path,
                        black_engine_path,
                        engine1_path,
                        engine2_path,
                    )
                white_time_control.apply_increment()
            case chess.BLACK:
                if black_time_control.time_as_secs <= 0:
                    game_result = conclude_game_timeout(
                        board,
                        white_engine_path,
                        black_engine_path,
                        black_time_control,
                        chess.BLACK,
                    )
                    return claim_winner(
                        game_result,
                        white_engine_path,
                        black_engine_path,
                        engine1_path,
                        engine2_path,
                    )
                start = time()
                best_move: Move = UCI_command.get_best_move(
                    black_engine, board, mutual_movetime
                )
                board.push(best_move)
                end = time()
                black_time_control.decrease_time(end - start)
                if black_time_control.time_as_secs <= 0:
                    game_result = conclude_game_timeout(
                        board,
                        white_engine_path,
                        black_engine_path,
                        black_time_control,
                        chess.BLACK,
                    )

                    return claim_winner(
                        game_result,
                        white_engine_path,
                        black_engine_path,
                        engine1_path,
                        engine2_path,
                    )
                black_time_control.apply_increment()

    game_pgn = chess.pgn.Game.from_board(board)
    game_result = game_pgn.headers["Result"]

    conclude_game(
        game_pgn,
        game_result,
        white_engine_path,
        black_engine_path,
        white_time_control.convert_to_pgn_time(),
        1850,
        1850,
    )
    return claim_winner(
        game_result,
        white_engine_path,
        black_engine_path,
        engine1_path,
        engine2_path,
    )
