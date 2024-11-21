def is_safe(board, row, col, N):
    # Check the same column
    for i in range(row):
        if board[i][col] == 1:
            return False
    
    # Check the upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N, 1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, row, N, solutions):
    # If all queens are placed successfully, store the solution
    if row >= N:
        solution = []
        for i in range(N):
            solution.append(''.join(' Q ' if board[i][j] else ' . ' for j in range(N)))
        solutions.append(solution)
        return
    
    # Try placing a queen in each column of the current row
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1  # Place the queen
            solve_n_queens_util(board, row + 1, N, solutions)
            board[row][col] = 0  # Backtrack

def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]  # Create an N x N chessboard
    solutions = []  # Store all solutions
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

N = 4
solutions = solve_n_queens(N)
for idx, solution in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    for row in solution:
        print(row)
    print()
