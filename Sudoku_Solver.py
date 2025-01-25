def is_valid(board,row,col,num):
    for x in range(9):
        if board[row][x] == num:
            return False
    for x in range(9):
        if board[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3) , 3 * (col // 3)
    for i in range(start_row,start_row + 3):
        for j in range(start_col,start_col + 3):
            if board[i][j] == num:
                return False
    return True
def sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board,row,col,num):
                        board[row][col] = num
                        if sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True
def printBoard(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))
def get_input():
    print("Enter the values for Sudoku Grid (use 0 for empty cells):")
    grid = []
    for i in range(9):
        while True:
            try:
                row = list(map(int, input(f"Row {i+1}: ").strip().split()))
                if len(row) != 9 or any(num < 0 or num > 9 for num in row):
                    raise ValueError("Each row must contains exactly 9 numbers between 0 and 9.")
                grid.append(row)
                break
            except ValueError as e:
                print(e)
    return grid
sudoku_grid = get_input()
print("\nUnsolved Sudoku:")
printBoard(sudoku_grid)
if sudoku(sudoku_grid):
    print("\nSolved Sudoku:")
    printBoard(sudoku_grid)
else:
    print("\nNo Solution exists!")
        
                
