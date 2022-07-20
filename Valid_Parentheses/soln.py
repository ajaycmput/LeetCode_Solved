"""
    Name: Nnamdi Ajoku
    Language: Python

    Description:Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

"""

def isValid(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace("()","").replace("[]","").replace("{}","")
    if s == "":
        result =  True
    else:
        result = False

    return result