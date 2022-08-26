"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given two strings ransomNote and magazine,
    
    return true if ransomNote can be constructed by using the 
    
    letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.

"""

def canConstruct(ransomNote, magazine):
    
    # dictionary
    track = {}
    # store each letter from magazine in a dictionary and count it
    for i in range(len(magazine)):
        if magazine[i]  in track:
            track[magazine[i]] =  track[magazine[i]]+1
        else:
            track[magazine[i]] = 1
    
    for j in range(len(ransomNote)):
        if ransomNote[j] in track and track[ransomNote[j]] != 0:
            track[ransomNote[j]] -= 1
        else:
            return False
        
    return True