#!/usr/bin/env python3
"""
Write a function that takes a string as input and reverse only the vowels of
a string.
"""


def reverseVowels(s: str) -> str:
    if not str:
        return ""

    charlist = list(s)
    p1 = 0
    p2 = len(charlist) - 1
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def swap(l, i, j):
        tmp = l[i]
        l[i] = l[j]
        l[j] = tmp

    while p1 < p2:
        while p1 < p2 and charlist[p1] not in vowels:
            p1 += 1
        while p1 < p2 and charlist[p2] not in vowels:
            p2 -= 1
        if charlist[p1] in vowels and charlist[p2] in vowels:
            swap(charlist, p1, p2)
            p1 += 1
            p2 -= 1

    return "".join(charlist)
