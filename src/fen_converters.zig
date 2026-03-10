const std = @import("std");
const board_repr = @import("board_repr.zig");
const piece_encoding = @import("piece_encoding.zig");

pub fn fen_to_board(fen_str: []const u8) !board_repr.BoardRepr {
    var board: board_repr.BoardRepr = board_repr.BoardRepr.empty();
    var split_fen = std.mem.splitAny(u8, fen_str, " ");

    const squares = split_fen.next() orelse return board;
    _ = split_fen.next(); // turn (color)
    _ = split_fen.next(); // caslting rights
    _ = split_fen.next(); // en passant
    const halfmove_clock = try std.fmt.parseInt(u8, split_fen.next().?, 10);
    const total_moves = try std.fmt.parseInt(u8, split_fen.next().?, 10);

    board.fifty_move = halfmove_clock / 2;
    board.move_counter = total_moves;

    var board_index: usize = 0;

    for (squares) |symbol| {
        if (std.ascii.isDigit(symbol)) {
            board_index += symbol - '0';
            continue;
        }
        const piece: u8 = switch (symbol) {
            'P' => piece_encoding.WHITE_PAWN,
            'B' => piece_encoding.WHITE_BISHOP,
            'N' => piece_encoding.WHITE_KNIGHT,
            'Q' => piece_encoding.WHITE_QUEEN,
            'K' => piece_encoding.WHITE_KING,
            'R' => piece_encoding.WHITE_ROOK,
            'p' => piece_encoding.BLACK_PAWN,
            'b' => piece_encoding.BLACK_BISHOP,
            'n' => piece_encoding.BLACK_KNIGHT,
            'q' => piece_encoding.BLACK_QUEEN,
            'k' => piece_encoding.BLACK_KING,
            'r' => piece_encoding.BLACK_ROOK,
            else => continue,
        };
        const row_reversed_index: usize = ((board_index / 8) * 8 + (8 - (board_index % 8))) - 1;
        board.pieces[row_reversed_index] = piece;
        board_index += 1;
    }

    return board;
}