import pygame
from .Constants import  DarkGreen,Rows,Cols,LightGreen ,Square_Size,White,Red
from .piece import Piece


class Board :
    def __init__(self):
        self.board =[]
        self.selected_piece = None
        self.red_left =self.white_left =12
        self.red_kings= self.red_kings=0
        self.create_board()


    def draw_cubes(self,win ):
            win.fill(DarkGreen)
            for row in range(Rows):
                for col in range(row%2,Rows,2):
                    pygame.draw.rect(win,LightGreen,(row * Square_Size,col * Square_Size,Square_Size,Square_Size))


    def create_board (self):
        for row in range (Rows):
            self.board.append([])
            for col in range (Cols):
                if col%2 ==((row+1)%2):
                    if row < 3 :
                        self.board[row].append(Piece(row,col,White))
                        
                    elif row > 4 :
                        self.board[row].append(Piece(row,col,Red))
                    else :
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)



    def draw(self,win):
        self.draw_cubes(win)
        for row in range(Rows):
            for col in range (Cols):
                piece =self.board[row][col]
                if piece!= 0 :
                    piece.draw(win)



