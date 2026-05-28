import chess
import logging
import uci_handler


def main() -> None:
    board = chess.Board()
    logging.basicConfig(
        filename="logs.txt",
        level=logging.DEBUG,
        format="%(levelname)s - %(message)s",
    )
    uci_handler.uci_manager(board)


if __name__ == "__main__":
    main()
