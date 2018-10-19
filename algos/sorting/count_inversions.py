"""
Counting inversions. An inversion in an array a[] is a pair of entries a[i]a[i]
and a[j]a[j] such that i < j but a[i] > a[j]
Given an array, design a linearithmic algorithm to count the # of inversions.
"""

"""
Use an enhanced version of merge sort

Programming Paradigm: Divide and Conquer

Perform merge sort steps
1. Divide Array
2. Call MergeSort on left and right halfs of array
3. Each step to merge sort should then return the # of inversions
4. The merge function - this is where it is different
   variants:
   - We know that we have two sorted arrays
   - If a[i] > a[j], then we know that
     there are mid - i inversions

     e.g
                mid
      i         j
     [4, 8, 9] [2, 10, 11]

     Because we know both are sorted there are mid - i
     invariants which is really just
     3 - 0 = 3 invariants when i == 0 and j === 3 and mid === 3
"""
