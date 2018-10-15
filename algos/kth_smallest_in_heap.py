#!/usr/bin/python3

"""
Problem: Given an array-based heap on n elements and a real number x,
efficiently determine whether the kth smallest element in the heap is
greater than or equal to x. Your algorithm should be O(k) in the worst-case,
independent of the size of the heap. Hint: you do not have to find the kth
smallest element; you need only determine its relationship to x.
"""

"""
Solution:

1. Extract min k times and test whether all of these nodes are less than x
"""
