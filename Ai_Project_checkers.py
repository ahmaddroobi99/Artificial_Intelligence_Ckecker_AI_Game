import pygame

from Checkers import board
from Checkers.Constants import Width, Height, Square_Size, Red
from  Checkers.game import Game
from Checkers.board import Board



FPS =60

Win =pygame.display.set_mode((Width,Height))

pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos) :
    x,y = pos
    row  =y//Square_Size
    col =x//Square_Size
    return row,col



def main ():
    run =True
    clock =pygame.time.Clock()
    # board= Board()
    game =Game(Win)

    # piece =board.get_piece(0,1)
    # board.move(piece ,4,3)


    while run :
        clock.tick(FPS)
        # pass
        if game.winner() != None:
            print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

            if event.type ==pygame.MOUSEBUTTONDOWN:
                # pass
                pos =pygame.mouse.get_pos()
                row ,col = get_row_col_from_mouse(pos)
                # if game.turn ==Red:
                game.select(row,col)
                # game.select(row, col)
                # piece =board.get_piece(row,col)
                # board.move(piece,4,3)
                
        # board.draw(Win)
        # pygame.display.update()
        game.update()

    pygame.quit()


main()
