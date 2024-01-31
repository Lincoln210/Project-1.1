def dfs_search(maze_dict):
    frontier = [] # frontier is a stack in DFS
    visited = set()
    start = maze_dict["start"]
    frontier.append(start, [start]) # the first element in this tuple keeps track of the node at the top of the stack, and the second element keeps track of the path taken to get to that node

    while frontier:
        position, path = frontier.pop()
        if position not in visited:
            visited.add(position)

        if position in maze_dict["goals"]:
            return path
        
        for neighbor in neighbors(position, maze_dict):
            if neighbor not in visited:
                frontier.append(neighbor, path.append(neighbor))

    return []

def neighbors(position, maze_dict):
    row = position[0]
    col = position[1]
    neighbors = []

    # move up
    if row > 0:
        neighbors.append((row - 1, col))

    # move down
    if row < maze_dict["rows"]:
        neighbors.append((row + 1, col))

    # move left
    if col > 0:
        neighbors.append((row, col - 1))

    # move right
    if col < maze_dict["cols"]:
        neighbors.append((row, col + 1))    

    return neighbors