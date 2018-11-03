"""Count the number of contiguous subsequences in an array that sum
up to a number k
"""
import unittest


def contiguous_subsequences(alist, k):
    """Args:
    alist: List[int]
    k: int
    """
    sum_map = {}
    res = 0
    curr_sum = 0
    # build the hash map of running sums the value is # of occurences
    for n in alist:
        curr_sum += n
        key = str(curr_sum)
        if key in sum_map:
            sum_map[key] += 1
        else:
            sum_map[key] = 1

    curr_sum = 0
    for n in alist:
        curr_sum += n
        target = str(curr_sum - k)

        if curr_sum == k:
            res += 1

        if target in sum_map:
            res += sum_map[target]

    return res

class ContiguousSubSequenceTest(unittest.TestCase):
    def test_contiguous_subsequences(self):
        a = [8, -1, -1, 9, 3, 4, -1]

        self.assertTrue(contiguous_subsequences(a, 6) == 2)


if __name__ == '__main__':
    unittest.main()
