"""
Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.
"""











"""
SOLUTION
- Create an array of indexes where the count of letters in the string is == 1
- Then return the minimum index
"""
def first_uniq_char(s):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    indexes = [s.index(letter) for letter in letters if s.count(letter) == 1]
    return min(indexes) if indexes else - 1

print(first_uniq_char("leetcode"))
print(first_uniq_char("loveleetcode"))
print(first_uniq_char("c"))
print(first_uniq_char("cc"))
