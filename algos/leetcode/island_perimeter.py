"""
You are given a map in form of a two-dimensional integer grid where 1
represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is
completely surrounded by water, and there is exactly one island (i.e., one or
more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water
around the island). One cell is a square with side length 1. The grid is
rectangular, width and height don't exceed 100. Determine the perimeter of
the island.
"""

"""
Solution: Iterate thru the matrix and for each land (where m[i][j] == 1).
Count # of edges that mean it's a perimeter

To count # of edges, get all neighbors for this point

For this point then iterate thru the 4 following cases mean that this
we can increase the count

1. x is < 0 (out of bounds)
2. y is < 0 (out of bounds)
3. x is on the outer left or right edge
4. y is on the upper edge
5. the adjacent is == 0 (it's water)
"""


def islandPerimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    if not grid:
        return 0

    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col]:
                count += sum_neighbors(grid, row, col)
    return count


def sum_neighbors(self, grid, row, col):
    adjacents = (row, col + 1), (row + 1, col), (row, col - 1), (row - 1, col)
    count = 0
    for x, y in adjacents:
        # look for number of edges
        if x < 0 or y < 0 or x == len(grid) or y == len(grid[0]) or grid[x][y] == 0:
            count += 1
    return count
