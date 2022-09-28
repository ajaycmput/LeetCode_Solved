"""
    Name: Nnamdi Ajoku
    Lnaguage: Python

    Description: Given a string s, reverse the order of characters in each word
    within a sentence while still preserving whitespace and initial word order.

"""

def reverseWords(s):
    track = {}
    count = 1
    string = ""
    for i in range(len(s)):
        if s[i] == " ":
            track[count] = string
            string = ""
            count += 1
        else:
            string +=s[i]
    track[count] = string
    
    # reverse each word in the dictionary (track)
    word_r = ""
    reversed_word = ""
    for v in track.values():
        for index in range(len(v)-1, -1, -1): # begin, end, decrement
            word_r += v[index]
        reversed_word += word_r
        word_r = " "
    return reversed_word