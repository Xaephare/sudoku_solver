#Sudoku solver

# Size of the grid (N*N)
GRIDSIZE = 9
# Size of smaller section
SECTIONSIZE = 3


def is_safe(grid, row, col, num):
    
    # Check if number is used in row
    for x in range(GRIDSIZE):
        if grid[row][x] == num:
            return False

    # Check if number is used in column
    for x in range(GRIDSIZE):
        if grid[x][col] == num:
            return False

    # Check if number is used in sectionsize*sectionsize grid
    start_row = row - row % SECTIONSIZE
    start_col = col - col % SECTIONSIZE
    for i in range(SECTIONSIZE):
        for j in range(SECTIONSIZE):
            if grid[i + start_row][j + start_col] == num:
                return False
    
    return True

def solve_sudoku(grid, row, col):
    # Base case: if we've reached the end of the grid, return True
    if row == GRIDSIZE:
        return True

    # If we've reached the end of a row, move to the next row
    if col == GRIDSIZE:
        return solve_sudoku(grid, row + 1, 0)

    # If the current cell is already filled, move to the next cell
    if grid[row][col] != 0:
        return solve_sudoku(grid, row, col + 1)

    # Try filling the current cell with each number from 1 to 9
    for num in range(1, 10):
        if is_safe(grid, row, col, num):
            grid[row][col] = num
            if solve_sudoku(grid, row, col + 1):
                return True
            grid[row][col] = 0

    # If no number worked, backtrack
    return False

grid = [[0, 8, 0, 0, 6, 7, 1, 0, 3],
        [0, 0, 4, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 4, 0, 0, 0, 1, 8, 0, 7],
        [5, 0, 0, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 9, 1, 0, 0, 3, 0, 6],
        [0, 3, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 6, 0, 4, 0]]

if solve_sudoku(grid, 0, 0):
    print(grid)
else:
    print("No solution exists.")