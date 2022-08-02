"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an n x n matrix where each of the rows and columns is sorted in ascending order,

    return the kth smallest element in the matrix.

    Note that it is the kth smallest element in the sorted order, not the kth distinct element.

    You must find a solution with a memory complexity better than O(n2).


    DISCLAIMER: The best approach is to use binary search and sort the 2D array with a single while loop. Another approach
                would be by collapsing the 2D matrix and sorting it and simply returning the matrix's kth element.

"""

from operator import add
from functools import reduce
def kthSmallest(matrix, k):
    row, col = 0, 0
    counter = 1

    matrix2 = reduce(add, matrix)
    matrix2.sort()

    i = 0
    while ( i < len(matrix2) and counter != k):
        i += 1
        counter += 1

    return matrix2[counter -1]