import pygame
from Checkers.Constants  import Width,Height
from Checkers.board import Board



FPS =60

Win =pygame.display.set_mode((Width,Height))

pygame.display.set_caption('Checkers')



def main ():
    run =True
    clock =pygame.time.Clock()
    board= Board()
    while run :
        clock.tick(FPS)
        pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run =False

            if event.type ==pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_cubes(Win)
        pygame.display.update()


    pygame.quit()


main()
