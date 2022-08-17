"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given a string s, find the first non-repeating character in it and return
    its index. If it does not exist, return -1.

"""

def firstUniqChar(s):
    
    track = {}
    for i in range(len(s)):
        if s[i] not in track:
            track[s[i]] = i
        else:
            track[s[i]] = -1
    
    count = 0
    for k,v in track.items():
        count += 1
        if v != -1:
            return track[k]
            break
        
        elif v == -1 and count == len(track):
            return v