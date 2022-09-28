"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: 
"""
import math
def trailingZeroes(n):
    
    num = str(math.factorial(n))
    count = 0
    for i in range( len(num)-1, -1, -1):
        if num[i] == "0":
            count+= 1
        else:
            break
    
    return count