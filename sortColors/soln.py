"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.

 

"""


def sortColors(nums):
    
    for i in range(0,len(nums)-1):
        
        j = i + 1
        while ( j <= len(nums) - 1):
            if nums[i] > nums[j]:
                temp = nums[i]
                
                nums[i] = nums[j]
                
                nums[ j ] = temp
                
                j += 1
            else:
                j += 1