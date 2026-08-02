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
    engine2_path = "engines/Ferrous_v0.5.0-dev6_qfix.exe"
    engine1_path = "engines/Ferrous_v0.5.0-dev8_lmr_fix.exe"
    engine1_won = 0
    engine2_won = 0
    engine1 = subprocess.Popen(
        [engine1_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )
    engine2 = subprocess.Popen(
        [engine2_path],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
    )

    for pos in starting_positions.STARTING_POSITIONS:
        print(f"playing position: {pos.fen}")
        board = chess.Board(pos.fen)
        score1, score2 = uci_handler.uci_manager(
            board,
            engine1,
            engine2,
            engine1_path.removesuffix(".exe").removeprefix("engines/"),
            engine2_path.removesuffix(".exe").removeprefix("engines/"),
            engine1_path.removesuffix(".exe").removeprefix("engines/"),
            engine2_path.removesuffix(".exe").removeprefix("engines/"),
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
            engine2_path.removesuffix(".exe").removeprefix("engines/"),
            engine1_path.removesuffix(".exe").removeprefix("engines/"),
            engine1_path.removesuffix(".exe").removeprefix("engines/"),
            engine2_path.removesuffix(".exe").removeprefix("engines/"),
            engine1_won,
            engine2_won,
        )
        engine1_won += score1
        engine2_won += score2

    print(
        f"{engine1}: {engine1_won} wins, {engine2_won} losses, {TOTAL_GAMES - (engine2_won + engine1_won)} draws"
    )


if __name__ == "__main__":
    try:
        main()
        print("the script has run successfully")
    except Exception as e:
        print(e)
    input()
