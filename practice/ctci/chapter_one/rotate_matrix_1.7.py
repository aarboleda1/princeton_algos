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


def rotate_matrix_(matrix):
    layers = len(matrix) // 2
    for layer in range(layers):
        end = len(matrix) - layer - 1
        start = layer
        for j in range(start, end):
            offset = j - start
            top = matrix[start][j]
            # bottom left -> top
            print(matrix[end - offset])
            matrix[start][j] = matrix[end - offset][start]
            # bottom right to bottom left
            matrix[end - offset][j] = matrix[end][end - offset]
            # top right to bottom right
            matrix[end][end - offset] = matrix[j][end]
            # top right
            matrix[j][end] = top
            print(matrix)

    return matrix

def rotate_matrix(matrix):
    '''rotates a matrix 90 degrees clockwise'''
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1
        for i in range(first, last):
            # save top
            top = matrix[layer][i]
            print(matrix[-i - 1])
            # left -> top
            matrix[layer][i] = matrix[-i - 1][layer]

            # bottom -> left
            matrix[-i - 1][layer] = matrix[-layer - 1][-i - 1]

            # right -> bottom
            matrix[-layer - 1][-i - 1] = matrix[i][- layer - 1]

            # top -> right
            matrix[i][- layer - 1] = top
    return matrix


class Test(unittest.TestCase):
    """Test Cases"""

    # Using lists because Python strings are immutable

    def test_matrix(self):
        data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        rotate_matrix_(data)
        self.assertListEqual(data[0], [7, 4, 1])
        self.assertListEqual(data[1], [8, 5, 2])
        self.assertListEqual(data[2], [9, 6, 3])


if __name__ == "__main__":
    unittest.main()
