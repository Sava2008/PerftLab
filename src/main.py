import chess
import logging
import uci_handler
import subprocess
import starting_positions

TOTAL_GAMES: int = 65 * 2


def main() -> None:
    logging.basicConfig(
        filename="logs.txt",
        level=logging.DEBUG,
        format="%(message)s",
    )
    engine1_path = "Ferrous_v0.4.0.exe"
    engine2_path = "Ferrous_v0.4.0-pre1.exe"
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
    uci_handler.UCI_command.has_uci(engine1)
    uci_handler.UCI_command.has_uci(engine2)
    for pos in starting_positions.STARTING_POSITIONS:
        if pos.assessment != starting_positions.PositionAssessment.equal:
            continue
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
        f"{engine1}: {engine1_won} wins, {engine2_won} losses, {TOTAL_GAMES - (engine2_won + engine1_won)} draws"
    )


if __name__ == "__main__":
    main()
