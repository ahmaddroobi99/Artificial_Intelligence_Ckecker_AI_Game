import pygame

from .Constants import DarkGreen,LightGreen ,Square_Size,Grey




class Piece :
    Padding = 15
    border =2


    def __init__(self,row,col,color):
        self.row = row
        self.col=col
        self.color=color
        self.king= False

        # if self.color==LightGreen :
        #     self.direction =-1
        # else:
        #     self.direction= 1


        self.x =0
        self.y = 0
        self.cal_pos()


    def cal_pos (self):
        self.x =Square_Size * self.col +Square_Size // 2
        self.y = Square_Size *self.row +Square_Size // 2

    def make_king(self):
        self.king =True

    def draw (self,win ):
        radius = Square_Size // 2 - self.Padding
        pygame.draw.circle(win ,Grey ,(self.x,self.y ),radius +self.border)
        pygame.draw.circle(win,self.color,(self.x,self.y),radius)

    def __repr__(self):
        return str(self.color)



