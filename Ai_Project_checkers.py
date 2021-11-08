import pygame
import tkinter as tk
from Checkers import board
from Checkers.Constants import Width, Height, Square_Size, Red, White
from Checkers.game import Game
from Checkers.board import Board
from MiniMax_AlphaBata_Algo.AlphBetaAlgorithm import miniMax
from tkinter import *

FPS = 60

Win = pygame.display.set_mode((Width, Height))

pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // Square_Size
    col = x // Square_Size
    return row, col


root = tk.Tk()
clicked = StringVar()
r = IntVar()


def main1():
    root.title('Checkers')
    root.geometry("300x100")

    r.set("4")
    Radiobutton(root, text="Easy      ", variable=r, value=2).pack(anchor=CENTER)
    Radiobutton(root, text="Medium", variable=r, value=3).pack(anchor=CENTER)
    Radiobutton(root, text="Hard      ", variable=r, value=4).pack(anchor=CENTER)
    MyBtn = Button(root, text="Select the difficulty ")
    MyBtn.pack(anchor=CENTER)

    root.mainloop()


def main2():
    run = True
    clock = pygame.time.Clock()
    # board= Board()
    game = Game(Win)

    # piece =board.get_piece(0,1)
    # board.move(piece ,4,3)

    while run:
        clock.tick(FPS)
        # pass
        if game.turn == White:
            value, new_board = miniMax(game.get_board(), 4, White, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # pass
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # if game.turn ==Red:
                game.select(row, col)
                # game.select(row, col)
                # piece =board.get_piece(row,col)
                # board.move(piece,4,3)

        # board.draw(Win)
        # pygame.display.update()
        game.update()

    pygame.quit()


main1()
main2()