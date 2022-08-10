"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: You are given a 0-indexed integer array nums. An index i is part of a hill in nums if the closest non-equal neighbors of i are smaller than nums[i]. Similarly, an index i is part of a valley in nums if the closest non-equal neighbors of i are larger than nums[i]. Adjacent indices i and j are part of the same hill or valley if nums[i] == nums[j].

    Note that for an index to be part of a hill or valley, it must have a non-equal neighbor on both the left and right of the index.

    Return the number of hills and valleys in nums.

    Code is faster than 99.52% of solutions



"""

def countHillValley(nums):
    count = 0

    i = 0
    k = i + 1
    j = i + 2

    while ( j <= len(nums)-1):
        idx = k
        if nums[k] == 101:
            nums[k] = original
            i += 1
            j += 1
            k += 1
        else:
            if nums[k] > nums[j] and nums[k] > nums[i]:
                count += 1
                i += 1
                j += 1
                k += 1

            elif nums[k] < nums[j] and nums[k] < nums[i]:
                    count += 1
                    i += 1
                    j += 1
                    k += 1

            else:
                while( idx < len(nums)-1):
                    if nums[k] == nums[idx+1] and nums[idx+1] != 101:
                        nums[idx+1] = 101 
                        original = nums[k]
                        idx += 1
                    else:
                        nums[idx] = nums[k]
                        if (nums[k] > nums[k-1] and nums[idx] > nums[idx+1]) or (nums[k] < nums[k-1] and nums[idx] < nums[idx+1]):
                            count += 1
                            break
                        break
                i += 1
                j += 1
                k += 1

    return count