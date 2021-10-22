import pygame
from .Constants import DarkGreen, Rows, Cols, LightGreen, Square_Size, White, Red
from .piece import Piece


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    def draw_cubes(self, win):
        win.fill(DarkGreen)
        for row in range(Rows):
            for col in range(row % 2, Rows, 2):
                pygame.draw.rect(
                    win,
                    LightGreen,
                    (row * Square_Size, col * Square_Size, Square_Size, Square_Size),
                )

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = (
            self.board[row][col],
            self.board[piece.row][piece.col],
        )
        piece.move(row, col)

        if row == Rows - 1 or row == 0:
            piece.make_king()
            if piece.color == White:
                self.white_kings = self.white_kings + 1
            else:
                self.red_kings = self.red_kings + 1

    def get_piece(self, row, col):
        return self.board[row][col]

    def create_board(self):
        for row in range(Rows):
            self.board.append([])
            for col in range(Cols):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, White))

                    elif row > 4:
                        self.board[row].append(Piece(row, col, Red))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_cubes(win)
        for row in range(Rows):
            for col in range(Cols):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == Red:
                    self.red_left -= 1
                else:
                    self.white_left -= 1

    def winner(self):
        if self.red_left <= 0:
            return White

        elif self.white_left <= 0:
            return Red

        return None

    def get_valid_movies(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == Red or piece.king:
            moves.update(
                self._traverse_left(row - 1, max(row - 3, -1), -1, piece.color, left)
            )
            moves.update(
                self._traverse_right(row - 1, max(row - 3, -1), -1, piece.color, right)
            )

        if piece.color == White or piece.king:
            moves.update(
                self._traverse_left(row + 1, min(row + 3, Rows), 1, piece.color, left)
            )
            moves.update(
                self._traverse_right(row + 1, min(row + 3, Rows), 1, piece.color, right)
            )

        return moves

    def _traverse_left(self, start, stop, step, color, left, skip_only=[]):
        moves = {}
        last = []

        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skip_only and not last:
                    break
                elif skip_only:
                    moves[(r, left)] = last + skip_only
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)

                    else:
                        row = min(r + 3, Rows)
                    moves.update(
                        self._traverse_left(
                            r + step, row, step, color, left - 1, skip_only=last
                        )
                    )
                    moves.update(
                        self._traverse_right(
                            r + step, row, step, color, left + 1, skip_only=last
                        )
                    )
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skip_only=[]):
        moves = {}
        last = []

        for r in range(start, stop, step):
            if right >= Cols:
                break
            current = self.board[r][right]
            if current == 0:
                if skip_only and not last:
                    break
                elif skip_only:
                    moves[(r, right)] = last + skip_only
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)

                    else:
                        row = min(r + 3, Rows)
                    moves.update(
                        self._traverse_left(
                            r + step, row, step, color, right - 1, skip_only=last
                        )
                    )
                    moves.update(
                        self._traverse_right(
                            r + step, row, step, color, right + 1, skip_only=last
                        )
                    )
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right -= 1
        return moves
