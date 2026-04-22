# Sudoku-Project

YOUTUBE LINK FOR DEMO: {The fitnessgramTM pacer test}

### JK Notes: 
Role: Board Generation / Difficulty / Logic

### RB Notes:
Role: FILL THIS ON YOUR OWN TIME

### TS Notes:
Role: FILL THIS ON YOUR OWN TIME

### JMC Notes:
Role: Rules and validation logic

    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.box_length = 3
        self.board = [[0] * row_length for _ in range(row_length)]


    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    def valid_in_box(self, row_start, col_start, num):
        for i in range(3):
            for j in range(3):
                if self.board[row_start + i][col_start + j] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        row_start = (row // 3) * 3
        col_start = (col // 3) * 3
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(row_start, col_start, num))
## Fork Repository Instructions
### Steps:
1. When you go to the github repository we provided, on the top right hand corner of the screen, there is a button that says "Fork". That will fork the repo to your own github 
2. Use the link https://github.com/new/import to clone your forked repo to make it private. You will work on the project by adding your own files to this private repository.

