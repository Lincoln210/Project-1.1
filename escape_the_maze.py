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

