import math

def minFallingPathSum(grid: list[list[int]]) -> int:
    n = len(grid)
    for row in range(1, n):
        # finds lowest and second lowest in the previous column
        lowest = second_lowest = math.inf
        lowest_col = None
        for index, num in enumerate(grid[row-1]):
            if num < lowest:
                lowest = num
                lowest_col = index
            if lowest < num < second_lowest:
                second_lowest = num
        print(grid[row-1])
        print(lowest, second_lowest)
        # adds the lowest possible value to each value in the current row
        for col in range(n):
            if col != lowest_col:
                grid[row][col] += second_lowest
            else:
                grid[row][col] += lowest
    return min(grid[n-1])

print(minFallingPathSum([[7]]))



