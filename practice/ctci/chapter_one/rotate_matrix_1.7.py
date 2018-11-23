import unittest
"""
Rotate Matrix 1.7
Given an image represented by an N x N Matrix, where each pixel in the image
is 4 bytes, write a method to rotate the image by 90 degress in place
[1, 2, 3, 4]
[5, 6, 7, 8]
[9, 10 , 11, 12]
[13, 14, 15, 16]
"""









"""Solution:
For each layer in the matrix, swap each pixel one by one
"""

def rotate_matrix(matrix):
    m_len = len(matrix)
    layers = int(len(matrix) / 2)
    for layer in range(0, layers):
        print("yoooooooo")
        last = m_len - layer - 1
        start = layer
        for j in range(start, last):
           offset = j - start
           top = matrix[start][j]
           # bottom left to top
           matrix[start][j] = matrix[last - offset][start]
           # bottom right to bottom left
           matrix[last - offset][j] = matrix[last][last - offset]
           # top right to bottom right
           matrix[last][last - offset] = matrix[j][last]
           # top right
           matrix[j][last] = top
           print(matrix)

    # print(matrix)


class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable

    def test_matrix(self):
        data = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        rotate_matrix(data)
        self.assertListEqual(data[0], [7, 4, 1])
        self.assertListEqual(data[1], [8, 5, 2])
        self.assertListEqual(data[2], [9, 6, 3])


if __name__ == "__main__":
    unittest.main()
