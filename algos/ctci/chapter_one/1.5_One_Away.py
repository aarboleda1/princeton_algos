#!/usr/bin/env python3
import unittest

def one_away(str1: str, str2: str) -> bool:
    if abs(len(str1) - len(str2)) > 1:
        return False
    s1 = str1 if len(str1) < len(str2) else str2
    s2 = str1 if s1 == str2 else str2
    # count how many off we are
    c = 0
    # pointers
    p1, p2 = 0, 0

    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] != s2[p2]:
            if c > 0:
                return False
            c = c + 1
            p2 = p2 + 1

        if s1[p1] == s2[p2]:
            p1 = p1 + 1
            p2 = p2 + 1

    return True


# OTHER SOLUTION FROM THE BOOK
# def one_away(str1: str, str2: str) -> bool:
#     if abs(len(str1) - len(str2)) > 1:
#         return False
#     s1 = str1 if len(str1) < len(str2) else str2
#     s2 = str1 if s1 == str2 else str2
#     # count how many off we are
#     found_diff = False
#     # pointers
#     p1, p2 = 0, 0
#
#     while p1 < len(s1) and p2 < len(s2):
#         if s1[p1] != s2[p2]:
#             if found_diff is True:
#                 return False
#             found_diff = True
#             if len(s1) == len(s2):
#                 p1 = p1 + 1
#         else:
#             # if the chars are the same, move shorter string pointer
#             p1 = p1 + 1
#
#         # always move longer pointer
#         p2 = p2 + 1

    return True
class OneAway(unittest.TestCase):
    def test_one_away(self):
        # Input keys (use only 'a' through 'z' and lower case)
        self.assertTrue(one_away("pale", "ple"))
        self.assertTrue(one_away("pale", "pales"))
        self.assertFalse(one_away("pale", "bake"))
        self.assertTrue(one_away("apple", "aple"))
        self.assertFalse(one_away("pale", "baked"))
        self.assertFalse(one_away("pale", "baking"))




if __name__ == '__main__':
    unittest.main()
