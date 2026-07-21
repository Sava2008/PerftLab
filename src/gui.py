import pygame as pg
from chess import BLACK, WHITE, Board
from pygame.color import Color
from pygame.rect import Rect
from pygame.surface import Surface


class ImmutableMeta(type):
    @classmethod
    def __setattr__(cls, name, value):
        raise PermissionError(
            f"unable to overwrite content of {type.__name__}"
        )

    @classmethod
    def __delattr__(cls, name, value):
        raise PermissionError(f"unable to delete content of {type.__name__}")


class ChessCoords(metaclass=ImmutableMeta):
    coords: tuple[str, ...] = tuple(
        letter + number
        for number in ("1", "2", "3", "4", "5", "6", "7", "8")
        for letter in ("a", "b", "c", "d", "e", "f", "g", "h")
    )

    @classmethod
    def move_to_uci(
        cls, from_idx: int, to_idx: int, promo: str | None = None
    ) -> str:
        uci_mv: str = cls.coords[from_idx] + cls.coords[to_idx]
        if promo is not None:
            uci_mv += promo
        return uci_mv


class InteractivePieces:
    grabbed_piece: int = 64


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
    return ((square % 8), (7 - (square // 8)))  # inverted coords


def calculate_index(x: int, y: int) -> int:
    normalized_x, normalized_y = (
        x // SQUARE_SIDE,
        8 - (y // SQUARE_SIDE + 1),
    )  # invert y, so that upper row = y::MAX

    return normalized_x + (8 * normalized_y)


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
            Rect(
                col * SQUARE_SIDE, row * SQUARE_SIDE, SQUARE_SIDE, SQUARE_SIDE
            ),
        )


def blit_individual_piece(
    screen: Surface, piece_idx: int, piece_bb: int
) -> None:
    while piece_bb != 0:
        piece_bb_trailing_zeros: int = (piece_bb & -piece_bb).bit_length()

        trailing_zeros_idx = piece_bb_trailing_zeros - 1

        white_piece_x: int
        white_piece_y: int
        white_piece_x, white_piece_y = (
            map(
                lambda x: x * SQUARE_SIDE,
                calculate_coords(trailing_zeros_idx),
            )
            if trailing_zeros_idx != InteractivePieces.grabbed_piece
            else map(lambda x: x - (0.5 * SQUARE_SIDE), pg.mouse.get_pos())
        )
        screen.blit(PIECE_IMAGES[piece_idx], (white_piece_x, white_piece_y))
        piece_bb &= piece_bb - piece_bb_trailing_zeros


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

        blit_individual_piece(screen, idx, white_occ & bb)
        blit_individual_piece(screen, idx + 6, black_occ & bb)


def grab_piece(mouse_x: int, mouse_y: int) -> None:
    InteractivePieces.grabbed_piece = calculate_index(mouse_x, mouse_y)


def place_piece(board: Board, mouse_x: int, mouse_y: int) -> None:
    final_pos = calculate_index(mouse_x, mouse_y)
    uci_move = ChessCoords.move_to_uci(
        InteractivePieces.grabbed_piece, final_pos
    )
    print(uci_move)
    if uci_move in board.legal_moves:
        board.push_uci(uci_move)

    InteractivePieces.grabbed_piece = 64


def play_against_engine(
    fen: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
) -> None:
    pg.init()
    screen: Surface = pg.display.set_mode((1280, 820))
    clock = pg.time.Clock()
    board: Board = Board(fen)

    running: bool = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        if pg.mouse.get_pressed()[0] and InteractivePieces.grabbed_piece == 64:
            mouse_x, mouse_y = pg.mouse.get_pos()
            if (
                mouse_x < 8 * SQUARE_SIDE and mouse_y < 8 * SQUARE_SIDE
            ):  # check if cursor is within board
                grab_piece(mouse_x, mouse_y)
        if (
            pg.mouse.get_just_released()[0]
            and InteractivePieces.grabbed_piece < 64
        ):
            mouse_x, mouse_y = pg.mouse.get_pos()
            if mouse_x < 8 * SQUARE_SIDE and mouse_y < 8 * SQUARE_SIDE:
                place_piece(board, mouse_x, mouse_y)
        screen.fill(BG_COLOR)
        draw_board(screen)
        blit_pieces(screen, board)

        pg.display.flip()
        clock.tick(60)

    pg.quit()


play_against_engine()
