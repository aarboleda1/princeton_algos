#!/usr/bin/env python3
import unittest
"""There are 3 types of edits that can be performed on strings
1) Insert a char
2) Remove a char
3) Replace a char

Given 2 strings, write a function to check if they are one edit away

Solution:
Base cases to cover
- We know that if the length of the strings differ by more than 1, they can't be
one away
    i.e. "abc" "abcdefg"
- Next we can divide it into 2 different sections
1. If the strings are the same length, we can iterate thru the two strings. and
return early if there are 2 chars that are different.
2. If they are not the same length, then use 2 pointers. and iterate thru both
strings so that, if we have found the "missing letter", mark the found_diff flag
to be true
"""
def one_away(str1: str, str2: str) -> bool:
    if abs(len(str1) - len(str2)) > 1:
        return False
    s1 = str1 if len(str1) < len(str2) else str2
    s2 = str1 if s1 == str2 else str2
    # count how many off we are
    found_diff = 0
    # pointers
    p1, p2 = 0, 0

    while p1 < len(s1) and p2 < len(s2):
        if s1[p1] != s2[p2]:
            if found_diff:
                return False
            found_diff = True
            p2 = p2 + 1

        if s1[p1] == s2[p2]:
            p1 = p1 + 1
            p2 = p2 + 1

    return True


# OTHER SOLUTION FROM THE BOOK
def one_away_alt(str1: str, str2: str) -> bool:
    if abs(len(str1) - len(str2)) > 1:
        return False
    if len(str1) == len(str2):
        found_diff = False
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                if found_diff:
                    return False
                else:
                    found_diff = True
        return True
    else:
        found_diff = False
        s1 = str1 if len(str1) < len(str2) else str2
        s2 = str1 if s1 == str2 else str2
        p1, p2 = 0, 0
        while p1 < len(s1) and p2 < len(s2):
            if s1[p1] != s2[p2]:
                if found_diff:
                    return False
                found_diff = True
                p2 = p2 + 1

            if s1[p1] == s2[p2]:
                p1 = p1 + 1
                p2 = p2 + 1
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

    def test_one_away_alt(self):
        # Input keys (use only 'a' through 'z' and lower case)
        self.assertTrue(one_away_alt("pale", "ple"))
        self.assertTrue(one_away_alt("pale", "pales"))
        self.assertFalse(one_away_alt("pale", "bake"))
        self.assertTrue(one_away_alt("apple", "aple"))
        self.assertFalse(one_away_alt("pale", "baked"))
        self.assertFalse(one_away_alt("pale", "baking"))




if __name__ == '__main__':
    unittest.main()
