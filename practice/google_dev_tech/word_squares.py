"""

https://techdevguide.withgoogle.com/resources/former-coding-interview-question-word-squares/?types=coding-interview-question#!

A “word square” is an ordered sequence of K different words of length K that,
 when written one word per line, reads the same horizontally and vertically.
 For example:
[
 "BALL",
 "AREA",
 "LEAD",
 "LADY",
]
"""






"""
Solution: Run all permutations of N
"""
def is_word_sq(words):
    if len(words) != len(words[0]):
        return False

    for i in range(len(words)):
        for j in range(len(words[0])):
            if words[i][j] != words[j][i]:
                return False
    return True


def all_word_squares(word_list, left, right):
    if left == right:
        if is_word_sq(word_list):
            return True
    # genereate all permutations of word_list where it equals 4
    for i in range(left, right):
        word_list[left], word_list[i] = word_list[i], word_list[left]
        all_word_squares(word_list, left + 1, right)
        word_list[left], word_list[i] = word_list[i], word_list[left]

print(is_word_sq([
 "BALL",
 "AREA",
 "LEAD",
 "LADY",
]))
print(all_word_squares(["AREA", "BALL", "DEAR", "LADY", "LEAD", "YARD"]))

print(is_word_sq([
 "BALS",
 "AREA",
 "LEAD",
 "LADY",
]))
