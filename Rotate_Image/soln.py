"""
    Name: Nnamdi Ajoku
    Language: Python3

    Description: You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.

"""

# import copy in order to use deepcopy
import copy

def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """

    row = len(matrix)-1
    col = 0
    # create a deepcopy of the initial matrix
    temp = copy.deepcopy(matrix)
    # since its an n x n matrix, we assume vertical = horizontal
    # hence horizonal and vertical satisfies the while loop condition
    while ( row >= 0):
        horizontal, vertical = 0, 0
        while ( horizontal <= len(matrix)-1):
            matrix[horizontal][col] = temp[row][vertical]

            horizontal += 1
            vertical += 1

        row -= 1
        col += 1