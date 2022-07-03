"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.
    Note:

    Only the space character ' ' is considered a whitespace character.
    Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

"""

def myAtoi(self, s: str) -> int:
    # declare a list that stores all digits
    atoi = ""
    isDigit = []
    isDigit = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9 }
    sign_multiplier = 1
    int_max = 2**31
    # check for any leading whitespaces
    for i in s:
        if i == " ":
            s = s.replace(i,"",1)
        else:
            break
    if len(s) > 0: # while we have not yet reached the end of the string
        # checking the sign of the first character ONLY
        for i in s:
            if i == "-":
                sign_multiplier = -1
                s = s.replace(i,"",1)
                break
            elif i == "+":
                s = s.replace(i,"",1)
                break
            else:
                break

        for j in s:
            if j  in isDigit:
                atoi = atoi + j
            else:
                break
        if len(atoi) <= 0:
            atoi = 0
        else:
            atoi = int(atoi)
    else:
        atoi = 0

    atoi = sign_multiplier*atoi

    #clamp to reamin in 32-bit signed int range (after work)
    if atoi >= -int_max and atoi <= int_max -1:
        atoi = atoi
    elif atoi <= -int_max:
        atoi = -int_max
    else:
        atoi = int_max -1

    return atoi


if __name__ == '__main__':
    myAtoi("00000-42a1234")