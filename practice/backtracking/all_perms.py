import unittest

"""Generate all permutations of a set


Solution:
Use backtracking

INPUT: "ABC"
OUTPUT: ['ABC', 'ACB', 'BAC', 'BCA', 'CBA', 'CAB']

 A
B  C

"""


def to_string(alist):
    return "".join(alist)


def permute(alist, left, right, result):
    if left == right:  # a check if is a solution
        return to_string(alist)  # process the solution
    else:
        for i in range(left, right):
            # make move
            alist[left], alist[i] = alist[i], alist[left]
            chars = permute(alist, left + 1, right, result)
            if chars is not None:
                result.append(chars)
            # unmake move/backtrack
            alist[i], alist[left] = alist[left], alist[i]


class AllPermsTestCase(unittest.TestCase):
    def test_all_perms(self):
        data = ["A", "B", "C"]
        result = []
        permute(data, 0, len(data), result)
        self.assertEquals(len(result), 6)
        print(result)


if __name__ == "__main__":
    unittest.main()
