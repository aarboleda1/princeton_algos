"""Generate all permutations of a set
"""

finished = False

import unittest
def all_perms_recur(alist, k, n, candidates):
    if is_a_solution(alist, k, n):
        process_solution(alist, k, candidates)
    else:
        k += 1
        construct_candidates()
        for i in range(len(candidates)):
            alist[k] = candidates[i]
            make_move(alist, k, candidates)
            unmake_move(alist, k, candidates)
            if finished:
                return

def construct_candidates():
    pass
def all_perms(alist):
    return all_perms_recur(alist, 0, len(alist), [])
def process_solution(alist, k, input):
    pass
def is_a_solution(k, n): # bool
    return k == n


class AllPermsTestCase(unittest.TestCase):
    def test_all_perms(self):
        pass
