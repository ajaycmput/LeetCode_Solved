"""
    Name: Nnamdi Ajoku
    Language: Python3

    Description: Given an array of integers nums containing
    
     n + 1 integers where each integer is in the range [1, n] inclusive.

    There is only one repeated number in nums, return this repeated number.

    You must solve the problem without modifying the array nums and uses only
    
    constant extra space.

 

"""
def findDuplicate(nums):
    track = {}
    
    for i in range(len(nums)):
        if nums[i] not in track:
            track[nums[i]] = nums[i]
        else:
            return nums[i]