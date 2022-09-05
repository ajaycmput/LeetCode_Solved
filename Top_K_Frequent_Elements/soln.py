"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an integer array nums and an integer k,
    
    return the k most frequent elements. You may return the answer in any order.

"""

def topKFrequent(nums, k):
    
    # create dict to store frequency of nums
    track = {}

    # result list
    res = []
    for i in nums:
        if i in track:
            track[i] = track[i] + 1
        else:
            track[i] = 1


    track_sorted = sorted(track.items(), key = operator.itemgetter(1), reverse = True)
    track_dict = dict(track_sorted)

    for keys,value in track_dict.items():
        if len(res) < k:
            res.append(keys)
        else:
            return res
        
    return res