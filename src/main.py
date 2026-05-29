import chess
import logging
import uci_handler
import subprocess
import starting_positions


def main() -> None:
    logging.basicConfig(
        filename="logs.txt",
        level=logging.DEBUG,
        format="%(levelname)s - %(message)s",
    )
    engine1_path = "Ferrous_v0.4.0-pre1.exe"
    engine2_path = "Ferrous_v0.4.0-pre1.exe"
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
        print(f"playing position: {pos.fen}")
        board = chess.Board(pos.fen)
        uci_handler.uci_manager(
            board, engine1, engine2, engine1_path, engine2_path
        )
        # uci_handler.uci_manager(board, engine2, engine2)


if __name__ == "__main__":
    main()
