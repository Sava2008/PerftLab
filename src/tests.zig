const std = @import("std");
const board_repr = @import("board_repr.zig");
const piece_encoding = @import("piece_encoding.zig");

test "simple move test" {
    var board: board_repr.BoardRepr = board_repr.BoardRepr.empty();
    board.pieces[0] = piece_encoding.WHITE_QUEEN;
    try board.move_piece(0, 3); // moving the queen to d1
    for (board.pieces, 0..board.pieces.len) |p, i| {
        if (i != 3) {
            try std.testing.expectEqual(p, piece_encoding.EMPTY_SQUARE);
            continue;
        } else {
            try std.testing.expectEqual(p, piece_encoding.WHITE_QUEEN);
        }
    }
}

test "capture test" {
    var board: board_repr.BoardRepr = board_repr.BoardRepr.empty();
    board.pieces[0] = piece_encoding.WHITE_QUEEN;
    board.pieces[2] = piece_encoding.BLACK_KNIGHT;
    try board.move_piece(0, 2); // moving the queen to c1
    for (board.pieces, 0..board.pieces.len) |p, i| {
        if (i != 2) {
            try std.testing.expectEqual(p, piece_encoding.EMPTY_SQUARE);
            continue;
        } else {
            try std.testing.expectEqual(p, piece_encoding.WHITE_QUEEN);
        }
    }
}

test "castling test" {
    var board: board_repr.BoardRepr = board_repr.BoardRepr.empty();
    board.pieces[60] = piece_encoding.BLACK_KING;
    board.pieces[56] = piece_encoding.BLACK_ROOK;
    try board.move_piece(60, 58); // moving the queen to c1
    for (board.pieces, 0..board.pieces.len) |p, i| {
        switch (i) {
            58 => try std.testing.expectEqual(p, piece_encoding.BLACK_KING),
            59 => try std.testing.expectEqual(p, piece_encoding.BLACK_ROOK),
            else => {
                try std.testing.expectEqual(p, piece_encoding.EMPTY_SQUARE);
            },
        }
    }
}
