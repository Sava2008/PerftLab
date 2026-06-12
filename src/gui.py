from typing import Generator

import pygame as pg
from chess import BLACK, WHITE, Board
from pygame.color import Color
from pygame.rect import Rect
from pygame.surface import Surface

SQUARE_SIDE: int = 100
LIGHT_SQUARE_COLOR: Color = Color(255, 235, 213)
DARK_SQUARE_COLOR: Color = Color(149, 75, 1)
BG_COLOR: str = "gray"
PIECE_IMAGES: tuple[Surface, ...] = tuple(
    pg.transform.scale(img, (SQUARE_SIDE, SQUARE_SIDE))
    for img in (
        pg.image.load(file_path)
        for file_path in (
            "pieces/white_pawn.png",
            "pieces/white_knight.png",
            "pieces/white_bishop.png",
            "pieces/white_rook.png",
            "pieces/white_queen.png",
            "pieces/white_king.png",
            "pieces/black_pawn.png",
            "pieces/black_knight.png",
            "pieces/black_bishop.png",
            "pieces/black_rook.png",
            "pieces/black_queen.png",
            "pieces/black_king.png",
        )
    )
)


def calculate_coords(square: int) -> tuple[int, int]:
    return ((square % 8), (7 - (square // 8)))


def draw_board(screen: Surface) -> None:
    for sq in range(64):
        col: int
        row: int
        col, row = calculate_coords(sq)
        sq_color: Color = (
            LIGHT_SQUARE_COLOR if col % 2 == row % 2 else DARK_SQUARE_COLOR
        )
        pg.draw.rect(
            screen,
            sq_color,
            Rect(col * SQUARE_SIDE, row * SQUARE_SIDE, SQUARE_SIDE, SQUARE_SIDE),
        )


def blit_pieces(screen: Surface, board: Board) -> None:
    white_occ: int = board.occupied_co[WHITE]
    black_occ: int = board.occupied_co[BLACK]
    all_pieces: tuple[int, int, int, int, int, int] = (
        board.pawns,
        board.knights,
        board.bishops,
        board.rooks,
        board.queens,
        board.kings,
    )
    for idx, bb in enumerate(all_pieces):
        if bb == 0:
            continue
        white_bb: int = white_occ & bb
        white_bb_trailing_zeros: int = (white_bb & -white_bb).bit_length()

        white_piece_x: int
        white_piece_y: int
        white_piece_x, white_piece_y = calculate_coords(white_bb_trailing_zeros)
        white_piece_x *= SQUARE_SIDE
        white_piece_y *= SQUARE_SIDE
        screen.blit(PIECE_IMAGES[idx], (white_piece_x, white_piece_y))

        black_bb: int = black_occ & bb
        black_bb_trailing_zeros: int = (black_bb & -black_bb).bit_length()

        black_piece_x: int
        black_piece_y: int
        black_piece_x, black_piece_y = calculate_coords(black_bb_trailing_zeros)
        black_piece_x *= SQUARE_SIDE
        black_piece_y *= SQUARE_SIDE
        screen.blit(PIECE_IMAGES[idx + 6], (black_piece_x, black_piece_y))


def play_against_engine() -> None:
    pg.init()
    screen: Surface = pg.display.set_mode((1280, 820))
    clock = pg.time.Clock()
    board: Board = Board(
        "rnbq1rk1/pppp1ppp/4pn2/8/1bPP4/2N5/PPQ1PPPP/R1B1KBNR w KQ - 4 5"
    )

    running: bool = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill(BG_COLOR)
        draw_board(screen)
        blit_pieces(screen, board)

        pg.display.flip()
        clock.tick(60)

    pg.quit()


play_against_engine()
