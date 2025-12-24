def is_safe(maze, x, y, n, visited):
    return (
        0 <= x < n and
        0 <= y < n and
        maze[x][y] == 1 and
        not visited[x][y]
    )

def solve_maze_util(maze, x, y, solution, n, visited):
    if x == n - 1 and y == n - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y, n, visited):
        solution[x][y] = 1
        visited[x][y] = True

        # Move Down
        if solve_maze_util(maze, x + 1, y, solution, n, visited):
            return True
        # Move Right
        if solve_maze_util(maze, x, y + 1, solution, n, visited):
            return True
        # Move Up
        if solve_maze_util(maze, x - 1, y, solution, n, visited):
            return True
        # Move Left
        if solve_maze_util(maze, x, y - 1, solution, n, visited):
            return True

        # Backtrack
        solution[x][y] = 0
        visited[x][y] = False
        return False

    return False

def solve_maze(maze):
    n = len(maze)
    solution = [[0 for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    if not solve_maze_util(maze, 0, 0, solution, n, visited):
        print("No path found")
        return

    print("Solution path:")
    for row in solution:
        print(row)

# Example maze 
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 0]
]

solve_maze(maze)


""" main_details = [{'mainstatus': None,
                  'mainstats':[{'mainid': 1, 'mainname': 'large', 'mainvalue':'afd46k' , 'mainstats': None}, 
                               {'mainid': 1,'mainname': 'heavy', 'mainvalue':'afd489k' , 'mainstats': [{'mainid': 1,'mainname': 'bigg', 'mainvalue':'afd111k', 'mainstats': None}, {'mainid': 1,'mainname': 'bigg', 'mainvalue':'afe45k' , 'mainstats': None}]},
                               {'mainid': 1,'mainname': 'small', 'mainvalue':'afd489k' , 'mainstats': None}]},
                {'mainstatus': None,
                  'mainstats':[{'mainid': 1, 'mainname': 'large', 'mainvalue':'afd36k' , 'mainstats': None}, 
                               {'mainid': 1,'mainname': 'heavy', 'mainvalue':'afd449k' , 'mainstats': [{'mainid': 1,'mainname': 'bigg', 'mainvalue':'bf222k', 'mainstats': None}, {'mainid': 1,'mainname': 'bigg', 'mainvalue':'afe45k' , 'mainstats': None}]},
                               {'mainid': 1,'mainname': 'small', 'mainvalue':'afd4889k' , 'mainstats': None}]}] """