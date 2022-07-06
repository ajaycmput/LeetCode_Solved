"""
Name: Nnamdi Ajoku
Language: Python

Description: Roman numerals are represented by seven different symbols:
I, V, X, L, C, D and M.

For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However,
the numeral for four is not IIII. Instead, the number four is written as IV. Because
the one is before the five we subtract it making four. The same principle applies to the
number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

"""
def romanToInt(self, s: str) -> int:
        # define roman numerals, INITIALIZATIONS
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        result = 0
        #edge cases
        i = 0
        while(i < len(s)):
            if s[i] == 'I':
                if i == (len(s)-1):
                    result = result + I
                    i = i +1
                else:
                    if s[i + 1] == 'V':
                        result = result + (V -I) #4
                        i = i + 2
                    elif s[i +1] == 'X':
                        result = result + (X - I) #9
                        i = i + 2
                    else: 
                        result = result + I
                        i = i + 1
            elif s[i] == 'X':
                if i == (len(s)-1):
                    result = result + X
                    i = i +1
                else:
                    if s[i + 1] == 'L':
                        result = result + (L-X) #40
                        i = i + 2
                    elif s[i +1] == 'C':
                        result = result + (C-X) #90
                        i = i + 2
                    else: 
                        result = result + X
                        i = i + 1
            elif s[i] == 'C':
                if i == (len(s)-1):
                    result = result + C
                    i = i +1
                else:
                    if s[i + 1] == 'D':
                        result = result + (D-C) #400
                        i = i + 2
                    elif s[i +1] == 'M':
                        result = result + (M-C) #900
                        i = i + 2
                    else: 
                        result = result + C
                        i = i + 1
            elif s[i] == 'V':
                result = result + V
                i = i + 1
            elif s[i] == 'L':
                result = result + L
                i = i + 1
            elif s[i] == 'D':
                result = result + D
                i = i + 1
            elif s[i] == 'M':
                result = result + M
                i = i + 1

        return result