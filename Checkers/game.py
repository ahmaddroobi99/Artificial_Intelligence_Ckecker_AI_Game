
import pygame
from .Constants import Red ,White
from Checkers.board import Board


class Game:
    def __init__(self ,Win):
        # self.selected = None
        # self.board =Board()
        # self.turn =Red
        # self.valid_moves ={ }
        self._init()
        self.Win =Win

    def update(self):
        self.board.draw(self.Win)
        pygame.display.update()

    def _init(self):
        self.selected = True
        self.board = Board()
        self.turn = Red
        self.valid_moves = {}

    def reset (self) :
       self._init(self)


    def select(self,row,col):
        if self.selected :
            result =self._move(row,col)
            if not result :
                self.selected =None
                self.select(row,col)

        else:
            piece = self.board.get_piece(row,col )
            if piece != 0and piece.color ==self.turn :
                self.selected =piece
                self.valid_moves= self.board.get_valid_moves (piece)
                return True

        return False




    def _move(self, row, col):
        piece = self.board.get_piece(row,col)
        if self.selected and piece == 0 and (row,col)in self.valid_moves:
            self.board.move(self.selected,row,col)
            self.change_turn()
            # skipped =self.valid_moves
        else :
            return False
        return True


    def change_turn (self):
        if self.turn ==Red :
            self.White
        else :
            self.turn = Red
