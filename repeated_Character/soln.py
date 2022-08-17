"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given a string s consisting of lowercase English letters, 
    return the first letter to appear twice.

"""
def repeatedCharacter(self, s: str) -> str:
    
    track = {}
    for i in range(0,len(s)):
        if s[i] in track.values():
            return s[i]
        else:
            track[i] = s[i]