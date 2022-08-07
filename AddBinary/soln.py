"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given two binary strings a and b, return their sum as a binary string.

"""
def addBinary(self, a: str, b: str) -> str:
    i = len(a)-1
    j = len(b)-1

    c_over = 0
    res = ""
    while( i >= 0 or j >= 0):

        if i < 0:
            first = 0
        else:
            first = int(a[i])

        if j < 0:
            second = 0
        else:
            second = int(b[j])

        summation = first + second + c_over

        carry = summation // 2

        bit = summation % 2

        res = str(bit) + res

        if carry > 0:
            c_over = carry
        else:
            c_over = 0  # default

        i-= 1
        j-= 1



    # if carry over is present

    if carry > 0:
        res = str(carry) + res

    return res