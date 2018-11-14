"""Implement a function to check if a linked list is a palindrome

Solution 1:
Use a stack to keep track of the 1st half of
elements. With the slow runner, at each step in the loop, we can push the data
from the slow runner into a stack. When fast runner reaches the end, we can then
iterate thru the 2nd half of the list and the values in the 2nd half of the list
with the values in the stack

Solution 2:
Create a reversed copy of the linked list. With this solution, we can iterate
thru the linked list and create a new, reversed version of the linked list. If
the lists are the same length, we could just iterate thru them at the same time
and return when they cross. Now, as long as we start at the same place in the
linked list, we can return at the first place where they match

1. Get lengths of each list get delta of the 2 lengths call it D
2. Compare the tails, if they do not equal each other, immediately return
3. With the longer linked list, advance its pointer by the difference in lengths
4. Iterate thru both lists and when you find a node intersects
"""

class Node:
    pass


def reverse_linked_list_clone(node):
    head = None
    while node is not None:
        n = Node(node.val)  # clone
        # Each node we insert into the linked list will either point to
        # None (if it is the first) or the last node we just created
        n.next = head
        # magic step hurr, by assigning to n, we're saving it for next iteration
        head = n
        node = node.next
    return head
