class Maze:
    def __init__(self, maze_dict):
        self.rows = maze_dict["rows"]
        self.cols = maze_dict["cols"]
        self.obstacles = set(tuple(obstacles) for obstacles in maze_dict["obstacles"])
        self.start = tuple(maze_dict["start"])
        self.goals = [tuple(goal) for goal in maze_dict["goals"]]