"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an integer n, return true if it is a power of four. Otherwise, return false.

    An integer n is a power of four, if there exists an integer x such that n == 4x.
"""
def isPowerOfFour(self, n: int) -> bool:
    result = False

    while( n % 4 == 0 and n > 1):

        n /= 4


    if n == 1:
        result = True

    return result