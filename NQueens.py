def is_safe(board, row, col, n):
    # Check this column in all previous rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n, solutions):
    if row == n:
        # Convert board into a readable solution
        solution = []
        for i in range(n):
            line = ''.join('Q' if cell == 1 else '.' for cell in board[i])
            solution.append(line)
        solutions.append(solution)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, solutions)
            board[row][col] = 0  # Backtrack

def n_queens(n):
    board = [[0] * n for _ in range(n)]
    solutions = []
    solve_n_queens(board, 0, n, solutions)
    return solutions

# Example usage
if __name__ == "__main__":
    N = int(input("Enter N (size of board): "))
    results = n_queens(N)
    print(f"\nNumber of solutions: {len(results)}")
    for idx, sol in enumerate(results, 1):
        print(f"\nSolution {idx}:")
        for row in sol:
            print(row)
