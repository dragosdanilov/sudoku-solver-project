def is_valid_move(grid, row, col, number):
    for x in range(9):
        if grid[row][x] == number:
            return False
        
    for y in range(9):
        if grid[col][y] == number:
            return False
        
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == number:
                return False
    return True

grid = [[2, 5, 0, 0, 8, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 9, 1, 0, 0, 0, 4, 2],
        [0, 0, 0, 0, 7, 8, 0, 9, 3],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 1, 6, 2, 0],
        [0, 7, 0, 0, 0, 0, 0, 0, 0],
        [0, 9, 0, 5, 0, 0, 8, 3, 0],
        [0, 1, 0, 9, 2, 0, 0, 0, 0]]