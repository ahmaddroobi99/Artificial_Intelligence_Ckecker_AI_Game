
import pygame
from .Constants import Red ,White ,Yellow ,Square_Size
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
        self.draw_valid_moves(self.valid_moves)
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


            piece = self.board.get_piece(row,col )
            if piece != 0and piece.color ==self.turn :
                self.selected =piece
                self.valid_moves= self.board.get_valid_movies (piece)
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

    def draw_valid_moves (self ,moves) :
        for move in moves :
            row ,col =move
            pygame.draw.circle(self.Win,Yellow,(col*Square_Size +Square_Size//2, row*Square_Size+Square_Size//2),10 )



    def change_turn (self):
        if self.turn ==Red :
            self.turn =White
        else :
            self.turn = Red
