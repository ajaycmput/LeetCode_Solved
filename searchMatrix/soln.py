"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

    Integers in each row are sorted in ascending from left to right.
    Integers in each column are sorted in ascending from top to bottom.

"""

def searchMatrix(matrix,target):
    # to decrease- move left or up
    # to increase- move right or down

    row, col = 0, len(matrix[0])-1
    while(row >= 0 and col >= 0 and row <= (len(matrix)-1) and col <= (len(matrix[0])-1)):
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col-=1
        else:
            row+=1
    return False