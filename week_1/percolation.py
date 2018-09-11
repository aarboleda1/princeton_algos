import unittest
from weighted_quick_union_uf import WeightedQuickUnionUF


class Percolation:
    def __init__(self, n):
        """create n-by-n grid, with all sites blocked
        """
        self.size = n
        self.bottom = self.size**2 + 1
        self.top = 0
        self.bottom = self.size**2 + 1
        self.opened = [[False for x in range(self.size)]
                       for x in range(self.size)]
        self.qf = WeightedQuickUnionUF(self.size**2 + 2)

    def open(self, row, col):  # None
        """open site (row, col) if it is not open already
        """
        self.validate(row, col)
        if row != 1 and self.isOpen(row - 1, col):
            self.qf.union(
                self.get_uf_index(row, col), self.get_uf_index(row - 1, col))
        if row < self.size and self.isOpen(row + 1, col):
            self.qf.union(
                self.get_uf_index(row, col), self.get_uf_index(row + 1, col))
        if col != 1 and self.isOpen(row, col - 1):
            self.qf.union(
                self.get_uf_index(row, col), self.get_uf_index(row, col - 1))
        if col > self.size and self.isOpen(row, col + 1):
            self.qf.union(
                self.get_uf_index(row, col), self.get_uf_index(row, col + 1))

    def get_uf_index(self, row, col):
        return self.size * (row - 1) + col

    def isOpen(self, row, col):  # bool
        """Is site (row, col) open?
        """

        # return self.grid[row, col].is_blocked

    def isFull():  # bool
        """is site (row, col) full?
        """
        pass

    def number_of_open_sites(self):  # int
        """number of open sites
        """
        # count = 0
        # [count_sites(row) for row in self.grid]
        pass

    def percolates():  # bool
        """does the system percolate?
        """
        pass

    def validate(self, row, col):
        """Validate that row/col is in the grid
        """
        if row < 1 or row > self.size or col < 1 or col > self.size:
            raise ValueError('Out of bounds array access!')


a = Percolation(5)
print(a.grid)
"""Weighted Quick Union Algorithm takes steps to avoid tall trees."""

if __name__ == '__main__':
    unittest.main()
