import logging
import subprocess

import chess

import starting_positions
import uci_handler

TOTAL_GAMES: int = len(starting_positions.STARTING_POSITIONS) * 2


def main() -> None:
    logging.basicConfig(
        filename="logs.txt",
        level=logging.DEBUG,
        format="%(message)s",
    )
    engine2_path = "Ferrous_v0.4.1.exe"
    engine1_path = "Ferrous_v0.5.0-dev.exe"
    engine1_won = 0
    engine2_won = 0
    engine1 = subprocess.Popen(
        [engine1_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    engine2 = subprocess.Popen(
        [engine2_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    for pos in starting_positions.STARTING_POSITIONS:
        print(f"playing position: {pos.fen}")
        board = chess.Board(pos.fen)
        score1, score2 = uci_handler.uci_manager(
            board,
            engine1,
            engine2,
            engine1_path,
            engine2_path,
            engine1_path,
            engine2_path,
            engine1_won,
            engine2_won,
        )
        engine1_won += score1
        engine2_won += score2
        print("reversing colors\n")
        board = chess.Board(pos.fen)
        score1, score2 = uci_handler.uci_manager(
            board,
            engine2,
            engine1,
            engine2_path,
            engine1_path,
            engine1_path,
            engine2_path,
            engine1_won,
            engine2_won,
        )
        engine1_won += score1
        engine2_won += score2

    print(
        f"{engine1_path}: {engine1_won} wins, {engine2_won} losses, {TOTAL_GAMES - (engine2_won + engine1_won)} draws"
    )


if __name__ == "__main__":
    try:
        main()
        print("the script has run successfully")
    except Exception as e:
        print(e)
    input()
