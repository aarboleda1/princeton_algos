class WeightedQuickUnionUF:
    def __init__(self, n):
        self.n = n
        self.array = list(range(n))
        self.size = {key: 0 for key in self.array}

    def connected(self, x, y):
        return self.__root(x) == self.__root(y)

    def union(self, x, y):
        i, j = self.__root(x), self.__root(y)
        if i == j:
            return
        elif self.size[i] < self.size[j]:
            self.array[i] = j
            self.size[j] += self.size[i]
        else:
            self.array[j] = i
            self.size[i] += self.size[j]

    def __root(self, i):
        while i != self.array[i]:
            self.array[i] = self.array[self.array[i]]
            i = self.array[i]
        return i
