from typing import Any, List

"""Quicksort

Not stable by default
"""


def quick_sort(arr: List[int], lo: int, hi: int) -> List[int]:  # noqa
    if lo < hi:
        j = partition(arr, lo, hi)
        quick_sort(arr, lo, j - 1)
        quick_sort(arr, j + 1, hi)
    return arr


def swap(arr: List[Any], i: int, j: int):  # noqa
    val = arr[i]
    arr[i] = arr[j]
    arr[j] = val

# Notice low - 1 and i + 1, This is done for list index so that index
# does not go out of bounds


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:

            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # final and important step, we can place pivot
    # in proper place in array
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)


a = quick_sort([8, 2, 1, 0], 0, 3)
print(a)

# Partition part 2

# def partition(arr: List[int], lo: int, hi: int) -> int:
#     """Find a partition element
#     - have two pointers a[i] -> left pointer a[j] -> right pointer
#
#     If a[i] is greater than partition element (a[lo]), stop because it is
#     out of place
#
#     If a[j] is less than partition element (a[lo]), stop because it is
#     out of place
#
#     Now, we can exchange a[i] with a[j] and keep our variant in place
#     -
#     """
#     i = lo
#     j = hi + 1
#     while (True):
#         # find item on the left to swap
#         while arr[i] < arr[lo]:
#             i += 1
#             if i == hi:
#                 break
#                 # find item on right to swap
#                 while arr[lo] < arr[j]:
#                     j -= 1
#                     if j == lo:
#                         break
#                         if i >= j:
#                             break
#                             arr[i + 1], arr[j] = arr[j], arr[i + 1]
#                             return j
