class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.col = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]