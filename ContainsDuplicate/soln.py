""" 
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.

"""

def containsDuplicate(nums):
    
    track = {}
    
    for i in nums:
        if i not in track:
            track[i] = 1
        else:
            return True
        
    return False