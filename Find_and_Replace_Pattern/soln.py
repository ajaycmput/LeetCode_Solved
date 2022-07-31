"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

    A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

    Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.
"""

def findAndReplacePattern(words, pattern):
    j = 0
    track = dict()
    res = []
    for i in pattern:
        if i not in track.values():
            track[j+1] = i
            j += 1

    patt_num = []
    for pat in pattern:
        for k,v in track.items():
            if pat == v:
                patt_num.append(str(k))

    track.clear()
    for word in words:
        index = 0
        for letter in word:
            if letter not in track.values():
                track[index+1] = letter
                index += 1
        code = []
        for letter in word:
            for k,v in track.items():
                if letter == v:
                    code.append(str(k))
        if patt_num == code:
            res.append(word)

        track.clear()
    
    return res

if __name__ ==  '__main__':
    findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")