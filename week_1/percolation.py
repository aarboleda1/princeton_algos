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
        self.opened[row - 1][col - 1] = True

        if (row == 1):
            self.qf.union(self.get_qf_index(row, col), self.top)
        elif (row == self.size):
            self.qf.union(self.get_qf_index(row, col), self.bottom)

        if row != 1 and self.is_open(row - 1, col):
            self.qf.union(
                self.get_qf_index(row, col), self.get_qf_index(row - 1, col))
        if row < self.size and self.is_open(row + 1, col):
            self.qf.union(
                self.get_qf_index(row, col), self.get_qf_index(row + 1, col))
        if col != 1 and self.is_open(row, col - 1):
            self.qf.union(
                self.get_qf_index(row, col), self.get_qf_index(row, col - 1))
        if col < self.size and self.is_open(row, col + 1):
            self.qf.union(
                self.get_qf_index(row, col), self.get_qf_index(row, col + 1))

    def get_qf_index(self, row, col):
        return self.size * (row - 1) + col

    def is_open(self, row, col):  # bool
        """Is site open
        """
        return self.opened[row - 1][col - 1]

    def is_full(self, i, j):
        if (i > 0 and i <= self.size and j > 0 and j <= self.size):
            return self.qf.connected(self.top, self.get_qf_index(i, j))
        else:
            return False

    def percolates(self):  # bool
        """does the system percolate?
        """
        return self.qf.connected(self.top, self.bottom)

    def validate(self, row, col):
        """Validate that row/col is in the grid
        """
        if row < 1 or row > self.size or col < 1 or col > self.size:
            raise ValueError('Out of bounds array access!')


class RandomValues:
    def __init__(self, n):
        values = list(range(1, n + 1))
        self.sample = []
        for y in values:
            self.sample += [[x, y] for x in values]


class PercolationTest(unittest.TestCase):
    def test_percolation(self):
        n = 5
        perc = Percolation(n)
        rv = RandomValues(n).sample
        print(rv)
        c = 0

        while (perc.percolates() is False):
            print(rv[c])
            perc.open(*rv[c])
            print(perc.percolates())
            c += 1
            print(perc.qf.array)

        print("Pecolates after " + str(c) + " attempts")


if __name__ == '__main__':
    unittest.main()
