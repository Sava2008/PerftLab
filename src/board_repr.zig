const piece_encoding = @import("piece_encoding.zig");

const IllegalMoveError = error{
    KingCaptureAttempt,
    EmptySquareCapture,
    IllegalCastling,
};

pub const BoardRepr = struct {
    pieces: [64]u8,
    fifty_move: u8 = 0,
    threefold: u8 = 0,
    move_counter: u16 = 0,
    material: i8,

    pub fn move_piece(self: *BoardRepr, from: usize, to: usize) !void {
        const starting_pos_piece: u8 = self.pieces[from];
        const ending_pos_piece: u8 = self.pieces[to];
        self.pieces[to] = starting_pos_piece;
        self.pieces[from] = piece_encoding.EMPTY_SQUARE;
        if (ending_pos_piece != 0) {
            try self.capture(ending_pos_piece);
            return;
        }
        const from_signed: i8 = @intCast(from);
        const to_signed: i8 = @intCast(to);
        if ((starting_pos_piece == piece_encoding.WHITE_KING or starting_pos_piece == piece_encoding.BLACK_KING) and @abs(from_signed - to_signed) > 1) {
            try self.castling(to);
        }
    }

    fn capture(self: *BoardRepr, ending_pos_piece: u8) !void {
        self.material += switch (ending_pos_piece) {
            piece_encoding.WHITE_PAWN => -1,
            piece_encoding.WHITE_BISHOP, piece_encoding.WHITE_KNIGHT => -3,
            piece_encoding.WHITE_ROOK => -5,
            piece_encoding.WHITE_QUEEN => -9,
            piece_encoding.BLACK_PAWN => 1,
            piece_encoding.BLACK_BISHOP, piece_encoding.BLACK_KNIGHT => 3,
            piece_encoding.BLACK_ROOK => 5,
            piece_encoding.BLACK_QUEEN => 9,
            piece_encoding.WHITE_KING, piece_encoding.BLACK_KING => return IllegalMoveError.KingCaptureAttempt,
            else => return IllegalMoveError.EmptySquareCapture,
        };
    }

    fn castling(self: *BoardRepr, king_final_pos: usize) !void {
        const rook_squares: struct { usize, usize } = switch (king_final_pos) {
            6 => .{
                7,
                5,
            }, // white O-O
            2 => .{
                0,
                3,
            }, // white O-O-O
            62 => .{
                63,
                61,
            }, // black O-O
            58 => .{
                56,
                59,
            }, // black O-O-O,
            else => return IllegalMoveError.IllegalCastling,
        };

        self.pieces[rook_squares[1]] = self.pieces[rook_squares[0]];
        self.pieces[rook_squares[0]] = piece_encoding.EMPTY_SQUARE;
    }

    pub fn empty() BoardRepr {
        return BoardRepr{
            .pieces = [64]u8{
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            },
            .fifty_move = 1,
            .threefold = 0,
            .move_counter = 0,
            .material = 0,
        };
    }
};
