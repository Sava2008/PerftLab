const std = @import("std");
const board_repr = @import("board_repr.zig");
const piece_encoding = @import("piece_encoding.zig");
const fen_converters = @import("fen_converters.zig");

pub fn main() void {
    std.debug.print("board {!}", .{fen_converters.fen_to_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")});
}
