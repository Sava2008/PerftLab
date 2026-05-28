import chess
import chess.pgn
import logging


def uci_manager(board: chess.Board) -> None:
    print("uci")
    if input() != "uciok":
        raise ValueError

    print("ready")
    if input() != "readyok":
        raise ValueError

    while True:
        if board.is_game_over():
            print("quit")
            logging.info(chess.pgn.Game.from_board(board))
            exit(0)
        print("go")
        best_move_mark, mv = input().split()

        if best_move_mark != "bestmove":
            raise ValueError("wrong uci encoding")

        best_move = chess.Move.from_uci(mv)
        if best_move in board.legal_moves:
            board.push(best_move)
        else:
            raise ValueError("illegal move {best_move}")
