"""
    Nmae: Nnamdi Ajoku
    Language: Python

    Description: You are given the strings key and message, which represent a cipher key and a secret message, respectively. The steps to decode message are as follows:

    Use the first appearance of all 26 lowercase English letters in key as the order of the substitution table.

    Align the substitution table with the regular English alphabet.

    Each letter in message is then substituted using the table.

    Spaces ' ' are transformed to themselves.
    
    For example, given key = "happy boy" (actual key would have at least one instance of each letter in the alphabet), we have the partial substitution table of ('h' -> 'a', 'a' -> 'b', 'p' -> 'c', 'y' -> 'd', 'b' -> 'e', 'o' -> 'f').

"""

import string
def decodeMessage(key,message):
    
    # generate alphabet dict
    track = dict.fromkeys(string.ascii_lowercase,0)
    
    # map keys in dictionary with numbers
    
    i = 1
    for k in track.keys():
        if i <= 26:
            track[k] = i
            i +=1
    
    record = {}
    letter = 0
    num = 1
    
    while letter <= len(key)-1:
        if key[letter] == " " or key[letter] in  record:
            letter += 1
        else:
            if num <= 26:
                record[key[letter]] = num
                num += 1
            
    # decode message
    code = ""
    for language in message:
        if language == " ":
            code += language
        else:
            for index, val in track.items():
                if val == record[language]:
                    code += index
                    break
            
    
    return code