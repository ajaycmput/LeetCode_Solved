"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

"""

def majorityElement(nums):
        
        times = len(nums) // 3
        
        res = []
        track = {}
        for i in nums:
            if i not in track:
                track[i] = 1
            else:
                track[i] = track[i] + 1
        
        for k in track.keys():
            if track[k] > times:
                res.append(k)
                
        return res