"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an array, rotate the array to the right by k steps, where k is non-negative.


"""

def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    count = 1
    while ( count <= k):
        elem = nums.pop()
        nums.insert(0, elem)
        count += 1