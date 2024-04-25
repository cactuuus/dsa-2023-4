def cavityMap(grid):
    """
    param: grid: an array of strings, representing a matrix of "depths"
    """
    for r in range(1, len(grid)-1):
        row = [c for c in grid[r]]
        for c in range(1, len(grid)-1):
            edges = [grid[r-1][c], grid[r+1][c], grid[r][c-1], grid[r][c+1]]
            if all(grid[r][c] > e for e in edges):
                row[c] = "X"
        grid[r] = "".join(row)
    return grid

cavityMap(['1112', '1912', '1892', '1234'])

