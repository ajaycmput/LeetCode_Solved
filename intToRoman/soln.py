"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, 2 is written as II in Roman numeral, just two one's added together.
    12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because the one
    is before the five we subtract it making four. The same principle applies to the number nine,
    which is written as IX. There are six instances where subtraction is used:

    I can be placed before V (5) and X (10) to make 4 and 9. 
    X can be placed before L (50) and C (100) to make 40 and 90. 
    C can be placed before D (500) and M (1000) to make 400 and 900.
    Given an integer, convert it to a roman numeral.

"""
def intToRoman(self, num: int) -> str:
    result = ""
    while(num != 0):
        if num >= 1000:
            result= result + "M"
            num = num - 1000
        # special case
        elif num >= 900 and num < 1000:
            result = result + "CM"
            num = num - 900
        elif num >= 500 and num < 900:
            result = result + "D"
            num = num- 500
        # special case
        elif num >= 400 and num < 500:
            result = result + "CD"
            num = num - 400
        elif num >= 100 and num < 400:
            result = result +"C"
            num = num -100
        # special case
        elif num >= 90 and num < 100:
            result = result + "XC"
            num = num - 90
        elif num >= 50 and num < 90:
            result = result + "L"
            num = num - 50
        # special case
        elif num >= 40 and num < 50:
            result = result + "XL"
            num = num - 40
        # special case
        elif num >= 10 and num < 40:
            result = result + "X"
            num = num - 10
        elif num >= 9 and num < 10:
            result= result + "IX"
            num = num - 9
        elif num >= 5 and num < 9:
            result = result + "V"
            num = num -5
        # special case
        elif num >= 4 and num < 5:
            result = result + "IV"
            num = num -4
        elif num >= 1 and num < 4:
            result = result + "I"
            num = num- 1

    return result



if __name__ == '__main__':
    intToRoman(1994)