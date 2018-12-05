"""
LRU Cache

An awesome tutorial/video
https://www.youtube.com/watch?v=7v_mUfpg46E&feature=youtu.be





Solution:

Data structures needed

2 Requirements: Constant time for get() and put() methods
for get we shoudl use a dict. That's a good structure for constant time access
For put(), we need could use a stack or a queue, but that's not constant time
we need to use a Linked List where we have access to the head and tail

We need the doubly linked list to be a doubly linked list so that we can remove
items from it

Have a convention where we say that anything to the left is least recently used
and anything to the right is most recently used

We use a dictionary/object where the value is the actual node. It's just a
pointer to the node which will give us constant time access

Simply create an _add method so that any time we add an item and add an item,
place it right after the head

For get, we remove then add. Why do we do this? Because add will always add the
item right before the tail making it the most recently used item
"""
