from sudoku_generator import *
import pygame as pg

def tilegen(difficulty):
    return generate_sudoku(9, difficulty)

def difficultyselect(difficulty):                                                                                       #0 = Easy, 1 = Medium, 2 = Hard
    if difficulty == 0:
        return 30
    elif difficulty == 1:
        return 40
    elif difficulty == 2:
        return 50

def windowgen():
    ...

def main():
    difficult = difficultyselect(0)                                                                                      # JK - Need someone to do stuff with PyGame for this, click EZ = 0, MED = 1, HRD = 2
    board = tilegen(difficult)
    print(board)

if __name__ == '__main__':
    main()