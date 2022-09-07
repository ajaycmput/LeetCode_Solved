"""
    Name: Nnamdi Ajoku
    Language: Python3

    Description: Given an unsorted integer array nums, return the smallest missing positive integer.

    You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""
def firstMissingPositive(nums):
    
    max_num = len(nums)
    
    track = {}
    for i in range(len(nums)):
        track[nums[i]] = nums[i]
        
    for j in range(1, max_num+2):
        if j not in track:
            return j