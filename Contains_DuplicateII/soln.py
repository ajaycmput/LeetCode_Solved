"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an integer array nums and an integer k,
    
    return true if there are two distinct indices i and j in the
    
    array such that nums[i] == nums[j] and abs(i - j) <= k.

"""
def containsNearbyDuplicate(nums,k ):
    
    # create dict
    track = {}
    
    for i in range(len(nums)):
        if nums[i] in track and abs(i - track[nums[i]] <= k ):
            return True
        
        track[nums[i]] = i 
    
    
    return False