import unittest


def merge_sort(alist):

    print("Splitting ", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

        return alist

    print("Merging ", alist)


# alist = [54,26,93,17,77,31,44,55,20]


class MergeSortTest(unittest.TestCase):
    def test_sort(self):
        arr = [8, 1, 2, 5, 0]
        sorted = merge_sort(arr)
        self.assertListEqual(sorted, [0, 1, 2, 5, 8], 'Incorrect!')


if __name__ == '__main__':
    unittest.main()
