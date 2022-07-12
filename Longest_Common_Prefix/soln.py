"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Write a function to find the longest common prefix string amongst an array of strings.

    If there is no common prefix, return an empty string "".

"""

def longestCommonPrefix(strs):
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        
        return res

if __name__ =='__main__':
    longestCommonPrefix(["aa", "ab"])