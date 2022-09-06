import copy
"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: A school is trying to take an annual photo of all the students.
    
    The students are asked to stand in a single file line in non-decreasing order by height. 
    
    Let this ordering be represented by the integer array expected where expected[i] is the 
    
    expected height of the ith student in line.

    You are given an integer array heights representing the current order that the students are standing in.
    
    Each heights[i] is the height of the ith student in line (0-indexed).

    Return the number of indices where heights[i] != expected[i].

"""

def heightChecker(heights):
    
    expected = copy.deepcopy(heights)
    expected.sort()
    
    lr, res = 0, 0
    while ( lr < len(expected) ):
        if heights[lr] != expected[lr]:
            res += 1
        
        lr += 1
    
    return res