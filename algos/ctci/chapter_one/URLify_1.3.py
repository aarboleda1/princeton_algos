"""Write a method to replac eall spaces in a string with `%20`. you may assume
that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.

Example:
Input: "Mr John Smith    " 13
Output: "Mr%20John%20Smith"
"""
"""SOLUTION:
Many string problems are used by editing from back to front. We'll do something
similar here.

1. Iterate thru the string, and increment num_spaces by 1. By keeping a count
of the # of spaces, we will then know the number of characters in the next string

2. Here is where we will edit the string. have 2 pointers. One that starts at
true length (i), and one at final length (j).

3. Iterate backwards thru the array. At each iteration: move s[i] to s[j] if not
space. otherwise add %20 to array

"""
import unittest

def urlify(s, true_length):
    new_index = len(s)
    for i in reversed(range(true_length)):
        if s[i] == ' ':
            s[new_index - 1] = '0'
            s[new_index - 2] = '2'
            s[new_index - 3] = '%'
            new_index -= 3
        else:
            s[new_index - 1] = s[i]
            new_index -= 1
    return s


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            # my_actual = _urlify(test_string, length)
            self.assertEqual(actual, expected)
            # self.assertEqual(my_actual, expected)

if __name__ == "__main__":
    unittest.main()
