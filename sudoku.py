from sudoku_generator import *
import pygame as pg
import sys

WIDTH = 630
HEIGHT = 750
BOARD_SIZE = 540
BOARD_X = 45
BOARD_Y = 100
CELL_SIZE = BOARD_SIZE // 9

BG_COLOR = (245, 247, 250)
LINE_COLOR = (0, 0, 0)
SELECT_COLOR = (220, 50, 50)
BUTTON_COLOR = (230, 140, 60)
BUTTON_TEXT_COLOR = (255, 255, 255)
FIXED_NUM_COLOR = (20, 20, 20)
USER_NUM_COLOR = (40, 90, 180)
TITLE_COLOR = (20, 20, 20)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Sudoku")

TITLE_FONT = pg.font.SysFont("arial", 40)
TEXT_FONT = pg.font.SysFont("arial", 26)
NUMBER_FONT = pg.font.SysFont("arial", 28)


def tilegen(difficult):
    return generate_sudoku(9, difficult)


def difficultyselect(difficulty):  # 0 = Easy, 1 = Medium, 2 = Hard
    if difficulty == 0:
        return 30
    elif difficulty == 1:
        return 40
    elif difficulty == 2:
        return 50


class Button:
    def __init__(self, x, y, w, h, text):
        self.rect = pg.Rect(x, y, w, h)
        self.text = text

    def draw(self, surface):
        pg.draw.rect(surface, BUTTON_COLOR, self.rect, border_radius=8)
        pg.draw.rect(surface, LINE_COLOR, self.rect, 2, border_radius=8)
        label = TEXT_FONT.render(self.text, True, BUTTON_TEXT_COLOR)
        label_rect = label.get_rect(center=self.rect.center)
        surface.blit(label, label_rect)

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


def draw_start_screen():
    screen.fill(BG_COLOR)

    title = TITLE_FONT.render("Welcome to Sudoku", True, TITLE_COLOR)
    subtitle = TEXT_FONT.render("Select Game Mode", True, TITLE_COLOR)

    screen.blit(title, title.get_rect(center=(WIDTH // 2, 180)))
    screen.blit(subtitle, subtitle.get_rect(center=(WIDTH // 2, 260)))

    easy_button = Button(90, 340, 120, 50, "Easy")
    medium_button = Button(255, 340, 120, 50, "Medium")
    hard_button = Button(420, 340, 120, 50, "Hard")

    easy_button.draw(screen)
    medium_button.draw(screen)
    hard_button.draw(screen)

    pg.display.update()
    return easy_button, medium_button, hard_button


def draw_board(board, selected, original_board):
    pg.draw.rect(screen, (255, 255, 255), (BOARD_X, BOARD_Y, BOARD_SIZE, BOARD_SIZE))

    for row in range(9):
        for col in range(9):
            value = board[row][col]
            if value != 0:
                if original_board[row][col] != 0:
                    color = FIXED_NUM_COLOR
                else:
                    color = USER_NUM_COLOR

                text = NUMBER_FONT.render(str(value), True, color)
                text_rect = text.get_rect(
                    center=(
                        BOARD_X + col * CELL_SIZE + CELL_SIZE // 2,
                        BOARD_Y + row * CELL_SIZE + CELL_SIZE // 2
                    )
                )
                screen.blit(text, text_rect)

    if selected is not None:
        row, col = selected
        x = BOARD_X + col * CELL_SIZE
        y = BOARD_Y + row * CELL_SIZE
        pg.draw.rect(screen, SELECT_COLOR, (x, y, CELL_SIZE, CELL_SIZE), 3)

    for i in range(10):
        thickness = 4 if i % 3 == 0 else 1

        x = BOARD_X + i * CELL_SIZE
        pg.draw.line(screen, LINE_COLOR, (x, BOARD_Y), (x, BOARD_Y + BOARD_SIZE), thickness)

        y = BOARD_Y + i * CELL_SIZE
        pg.draw.line(screen, LINE_COLOR, (BOARD_X, y), (BOARD_X + BOARD_SIZE, y), thickness)


def draw_game_screen(board, selected, original_board):
    screen.fill(BG_COLOR)

    title = TEXT_FONT.render("Sudoku", True, TITLE_COLOR)
    screen.blit(title, (45, 45))

    draw_board(board, selected, original_board)

    reset_button = Button(100, 670, 110, 45, "Reset")
    restart_button = Button(260, 670, 110, 45, "Restart")
    exit_button = Button(420, 670, 110, 45, "Exit")

    reset_button.draw(screen)
    restart_button.draw(screen)
    exit_button.draw(screen)

    pg.display.update()
    return reset_button, restart_button, exit_button


def click_to_cell(x, y):
    if BOARD_X <= x <= BOARD_X + BOARD_SIZE and BOARD_Y <= y <= BOARD_Y + BOARD_SIZE:
        col = (x - BOARD_X) // CELL_SIZE
        row = (y - BOARD_Y) // CELL_SIZE
        return row, col
    return None


def windowgen():
    clock = pg.time.Clock()
    state = "start"

    board = None
    original_board = None
    selected = None

    easy_button, medium_button, hard_button = draw_start_screen()
    reset_button = None
    restart_button = None
    exit_button = None

    while True:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if state == "start":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()

                    if easy_button.clicked(pos):
                        difficult = difficultyselect(0)
                        board = tilegen(difficult)
                        original_board = [row[:] for row in board]
                        selected = None
                        state = "game"

                    elif medium_button.clicked(pos):
                        difficult = difficultyselect(1)
                        board = tilegen(difficult)
                        original_board = [row[:] for row in board]
                        selected = None
                        state = "game"

                    elif hard_button.clicked(pos):
                        difficult = difficultyselect(2)
                        board = tilegen(difficult)
                        original_board = [row[:] for row in board]
                        selected = None
                        state = "game"

            elif state == "game":
                if event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()

                    clicked_cell = click_to_cell(pos[0], pos[1])
                    if clicked_cell is not None:
                        selected = clicked_cell

                    elif reset_button is not None and reset_button.clicked(pos):
                        board = [row[:] for row in original_board]
                        selected = None

                    elif restart_button is not None and restart_button.clicked(pos):
                        state = "start"
                        board = None
                        original_board = None
                        selected = None

                    elif exit_button is not None and exit_button.clicked(pos):
                        pg.quit()
                        sys.exit()

                elif event.type == pg.KEYDOWN:
                    if selected is None:
                        selected = (0, 0)

                    row, col = selected

                    if event.key == pg.K_LEFT:
                        selected = (row, max(0, col - 1))
                    elif event.key == pg.K_RIGHT:
                        selected = (row, min(8, col + 1))
                    elif event.key == pg.K_UP:
                        selected = (max(0, row - 1), col)
                    elif event.key == pg.K_DOWN:
                        selected = (min(8, row + 1), col)
                    elif original_board[row][col] == 0:
                        if event.unicode in "123456789":
                            board[row][col] = int(event.unicode)
                        elif event.key == pg.K_BACKSPACE or event.key == pg.K_DELETE:
                            board[row][col] = 0

        if state == "start":
            easy_button, medium_button, hard_button = draw_start_screen()
        elif state == "game":
            reset_button, restart_button, exit_button = draw_game_screen(board, selected, original_board)


def main():
    windowgen()


if __name__ == '__main__':
    main()
