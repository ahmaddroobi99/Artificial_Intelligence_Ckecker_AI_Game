import pygame
from .Constants import  DarkGreen,Rows,Cols,LightGreen ,Square_Size

class Board :
    def __init__(self):
        self.board =[]
        self.selected_piece = None
        self.red_left =self.white_left =12
        self.red_kings= self.red_kings=0


    def draw_cubes(self,win ):
            win.fill(DarkGreen)
            for row in range(Rows):
                for col in range(row%2,Rows,2):
                    pygame.draw.rect(win,LightGreen,(row * Square_Size,col * Square_Size,Square_Size,Square_Size))


    def create_board (self):
        pass


