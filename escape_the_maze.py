class Maze:
    def __init__(self, rows, cols):
        if rows > 1101 or cols > 1101:
            raise ValueError("Maximum size of maze must be 1101 x 1101")
        self.rows = rows
        self.col = cols
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]