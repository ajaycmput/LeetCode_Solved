"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.
"""

def isPalindrome(x):
    int_string = str(x)
    j = len(int_string) -1
    i = 0
    result = False
    while(i <= j):
        if (int_string[i] == int_string[j]):
            result = True
            i = i +1
            j = j-1
        else:
            result = False
            break

    return result



if __name__ =='__main__':
    isPalindrome(2244334422)