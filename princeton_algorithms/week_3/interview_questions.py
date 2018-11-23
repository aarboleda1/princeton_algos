"""Week 3 Interview Questions"""

"""
Dynamic median. Design a data type that supports insert in logarithmic time,
find-the-median in constant time, and remove-the-median in logarithmic time.
"""

"""
Design:

    2 Binary Heaps!

    use a min-heap and a max-heap
Insert - check # of nodes in two heaps,
    - if they are equal, insert into minheap
    - otherwise, insert into heap with lesser nodes
Remove Median -
    - Case:
        # of nodes are equal
    - Case:
        # Not equal. Call pop on heap with more nodes
Find Median:
    - More nodes: pop()
    - nodes are equal in both heaps, get min
"""
