"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.
"""

def twoSum(nums, target):
        sorted_list = []
        for i in nums:
            sorted_list.append(i)
        sorted_list.sort()
        nums = dict(enumerate(nums))
        start = 0
        end = len(sorted_list)-1
        result = []
        while(start < end):
            if (sorted_list[start] + sorted_list[end])> target:
                end = end-1
            elif (sorted_list[start] + sorted_list[end]) < target:
                start = start+ 1
            else:
                for k in nums:
                    if nums[k] == sorted_list[start]:
                        result.append(k)
                    if sorted_list[start] != sorted_list[end]:
                        if nums[k] ==sorted_list[end]:
                            result.append(k)
                return result