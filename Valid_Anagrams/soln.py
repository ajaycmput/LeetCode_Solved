'''
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

    An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
    typically using all the original letters exactly once.

'''
def isAnagram(self, s: str, t: str) -> bool:
    list1 = sorted(s)
    list2 = sorted(t)
    
    string1 = ''.join(list1)
    string2 = ''.join(list2)
    
    if string1 == string2:
        return True
    else :
        return False