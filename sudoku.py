import random

def is_valid(board, r, c, num):
    # 행, 열, 3x3 영역에 같은 숫자가 존재하는지 확인
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False
    
    start_row, start_col = 3 * (r // 3), 3 * (c // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def solve(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for num in range(1, 10):
                    if is_valid(board, r, c, num):
                        board[r][c] = num
                        if solve(board):
                            return True
                        board[r][c] = 0
                return False
    return True

def generate_sudoku():
    board = [[0] * 9 for _ in range(9)]
    solve(board)
    return board

def remove_numbers(board, difficulty):
    count = 81 - difficulty
    while count > 0:
        r, c = random.randint(0, 8), random.randint(0, 8)
        if board[r][c] != 0:
            board[r][c] = 0
            count -= 1
    return board

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

# 예시: 난이도 40으로 스도쿠 생성
difficulty = 30
board = generate_sudoku()
board = remove_numbers(board, difficulty)
print_board(board)
