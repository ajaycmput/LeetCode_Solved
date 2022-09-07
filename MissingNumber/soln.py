"""
    Name: Nnamdi Ajoku
    Language: Python

    Description:

"""

def missingNumber(nums):
    
    max_num = len(nums)
    
    track = {}
    
    for i in nums:
        if i not in track:
            track[i] = i
        else:
            continue
    
    for i in range( 0, max_num+1):
        if i not in track:
            return i