import pygame as pg
from chess import BLACK, WHITE, Board, Move, InvalidMoveError
from pygame.color import Color
from pygame.rect import Rect
from pygame.surface import Surface

SQUARE_SIDE: int = 100
BOARD_SIDE_LEN: int = SQUARE_SIDE * 8

LIGHT_SQUARE_COLOR: Color = Color(255, 235, 213)
DARK_SQUARE_COLOR: Color = Color(149, 75, 1)
MOVE_HIGHLIGHT_COLOR: Color = Color(51, 117, 135, 180)
FROM_SQ_HIGHLIGHT_COLOR: Color = Color(79, 96, 120, 150)
CAPTURE_HIGHLIGHT_COLOR: Color = Color(186, 62, 0, 200)

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


class InteractivePieces:
    grabbed_piece: int | None = None
    promotion_piece: str | None = None
    selected_legal_moves: list[Move] = []

    @classmethod
    def fill_legal_moves(cls, board: Board) -> None:
        if cls.grabbed_piece is None:
            return None
        cls.selected_legal_moves = list(
            board.generate_legal_moves(from_mask=1 << cls.grabbed_piece)
        )

    @classmethod
    def grab_piece(cls, board: Board, mouse_x: int, mouse_y: int) -> None:
        cls.grabbed_piece = calculate_index(mouse_x, mouse_y)
        cls.fill_legal_moves(board)

    @classmethod
    def place_piece(cls, board: Board, mouse_x: int, mouse_y: int) -> None:
        final_pos = calculate_index(mouse_x, mouse_y)
        if cls.grabbed_piece is None:
            raise ValueError(
                f"called place_piece before assigning a value to {cls.__name__}.grabbed_piece"
            )
        uci_move = ChessCoords.move_to_uci(cls.grabbed_piece, final_pos)

        try:
            if (
                uci_move is not None
                and Move.from_uci(uci_move) in board.legal_moves
                and mouse_x <= BOARD_SIDE_LEN
            ):
                board.push_uci(uci_move)
        except InvalidMoveError, TypeError:  # uci_move can be None
            pass  # let the player make another move

        cls.grabbed_piece = None
        cls.promotion_piece = None


class ImmutableMeta(type):
    @classmethod
    def __setattr__(cls, name, value) -> None:
        raise PermissionError(
            f"unable to overwrite content of {type.__name__}"
        )

    @classmethod
    def __delattr__(cls, name, value) -> None:
        raise PermissionError(f"unable to delete content of {type.__name__}")


class ChessCoords(metaclass=ImmutableMeta):
    coords: tuple[str, ...] = tuple(
        letter + number
        for number in ("1", "2", "3", "4", "5", "6", "7", "8")
        for letter in ("a", "b", "c", "d", "e", "f", "g", "h")
    )
    scalar_coords: tuple[tuple[int, int], ...] = tuple(
        (x * SQUARE_SIDE, y * SQUARE_SIDE)
        for y in range(7, -1, -1)
        for x in range(0, 8)
    )

    @classmethod
    def move_to_uci(cls, from_idx: int, to_idx: int) -> str | None:
        if to_idx > 63:
            return None
        uci_mv: str = cls.coords[from_idx] + cls.coords[to_idx]
        if InteractivePieces.promotion_piece is not None and (
            to_idx < 8 or to_idx > 55
        ):
            uci_mv += InteractivePieces.promotion_piece
        return uci_mv


def calculate_coords(square: int) -> tuple[int, int]:
    return ((square % 8), (7 - (square // 8)))  # inverted coords


def calculate_index(x: int, y: int) -> int:
    normalized_x, normalized_y = (
        x // SQUARE_SIDE,
        8 - (y // SQUARE_SIDE + 1),
    )  # invert y, so that upper row = y::MAX

    return normalized_x + (8 * normalized_y)


def draw_board(screen: Surface, board: Board) -> None:
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

    if InteractivePieces.grabbed_piece is not None:
        blit_highlights(screen, board)


def blit_individual_piece(
    screen: Surface, piece_idx: int, piece_bb: int
) -> None:
    while piece_bb != 0:
        piece_bb_trailing_zeros: int = (piece_bb & -piece_bb).bit_length()

        trailing_zeros_idx = piece_bb_trailing_zeros - 1

        white_piece_x: int
        white_piece_y: int
        white_piece_x, white_piece_y = (
            ChessCoords.scalar_coords[trailing_zeros_idx]
            if trailing_zeros_idx != InteractivePieces.grabbed_piece
            else map(lambda x: x - (SQUARE_SIDE // 2), pg.mouse.get_pos())
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


def blit_highlights(screen: Surface, board: Board) -> None:
    if len(InteractivePieces.selected_legal_moves) < 1:
        return

    from_x: int
    from_y: int
    to_x: int
    to_y: int

    from_x, from_y = calculate_coords(
        InteractivePieces.selected_legal_moves[0].from_square
    )
    highlight_surface = pg.Surface((SQUARE_SIDE, SQUARE_SIDE), pg.SRCALPHA)
    highlight_surface.fill(FROM_SQ_HIGHLIGHT_COLOR)
    screen.blit(
        highlight_surface, (from_x * SQUARE_SIDE, from_y * SQUARE_SIDE)
    )

    for piece_move in InteractivePieces.selected_legal_moves:
        to_x, to_y = ChessCoords.scalar_coords[piece_move.to_square]
        highlight_surface.fill(
            MOVE_HIGHLIGHT_COLOR
            if board.piece_at(piece_move.to_square) is None
            else CAPTURE_HIGHLIGHT_COLOR
        )
        screen.blit(
            highlight_surface, (to_x * SQUARE_SIDE, to_y * SQUARE_SIDE)
        )


def play_against_engine(
    fen: str = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1",
) -> None:
    pg.init()
    screen: Surface = pg.display.set_mode((1280, 820), pg.SRCALPHA)
    clock = pg.time.Clock()
    board: Board = Board(fen)
    game_font: pg.Font = pg.font.SysFont("Consolas", 15)

    # time tracking
    last_time_updated: int = 0
    current_time: int = 0

    fps: int = 60

    running: bool = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if (
                event.type == pg.KEYDOWN
                and InteractivePieces.grabbed_piece is not None
                and board.piece_type_at(InteractivePieces.grabbed_piece) == 1
            ):
                InteractivePieces.promotion_piece = (
                    "q"
                    if event.key == pg.K_q
                    else "r"
                    if event.key == pg.K_r
                    else "b"
                    if event.key == pg.K_b
                    else "n"
                    if event.key == pg.K_n
                    else None
                )

        if (
            pg.mouse.get_pressed()[0]
            and InteractivePieces.grabbed_piece is None
        ):
            mouse_x, mouse_y = pg.mouse.get_pos()
            if (
                mouse_x < BOARD_SIDE_LEN and mouse_y < BOARD_SIDE_LEN
            ):  # check if cursor is within board
                InteractivePieces.grab_piece(board, mouse_x, mouse_y)
        if (
            pg.mouse.get_just_released()[0]
            and InteractivePieces.grabbed_piece is not None
        ):
            mouse_x, mouse_y = pg.mouse.get_pos()
            InteractivePieces.place_piece(board, mouse_x, mouse_y)
        screen.fill(BG_COLOR)
        draw_board(screen, board)
        blit_pieces(screen, board)
        fps_chart = game_font.render(f"{fps} fps", True, "white")
        screen.blit(
            fps_chart,
            (1200, 5),
        )

        # update fps counter once per second
        current_time = pg.time.get_ticks()
        if current_time - last_time_updated >= 1000:
            last_time_updated = current_time
            fps = int(clock.get_fps())

        pg.display.flip()
        clock.tick(60)

    pg.quit()


play_against_engine()
