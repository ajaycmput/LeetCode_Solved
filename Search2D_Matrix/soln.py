"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: 

"""

def searchMatrix(matrix, target):
    
    # easy binary search
    
    row, col = 0, len(matrix[0])-1
    while (row >= 0 and col >= 0 and row <= (len(matrix)-1) and col <= (len(matrix[0])-1)):
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] > target:
            col -= 1
        else:
            row += 1
            
    return False