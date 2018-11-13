#!/usr/bin/env python3
"""
2.7 Intersection
Given two (singly) linked lists, determine if the two lists
intersect. Return the intersecting node. Note that the intersection is
defined based on reference, not value. That is, if the kth node of the first
linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""
















"""

Solution:
If you draw out 2 examples. 1 where linkedlists intersect and one where they
do not, the one that intersects will always have the tails be the same

So, we could traverse thru each of the lists. When we see tails then we can
traverse backwards and return when the nodes are not equal. EXCEPT, you can't
actually traverse backwards thru 2 linked lists

The solution is:
1. Check that tails are same if not, return None
2. Find delta "d" in lengths between 2 lists
3. Advance pointer for longer list "d" times
4. Traverse both pointers thru the list. Always looking curr.next if both curr.next'
match, then return curr
"""
