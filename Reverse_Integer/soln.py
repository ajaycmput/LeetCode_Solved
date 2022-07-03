"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes
    the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

"""

def reverse(self,x):
    result = 0
    sign_change = 1
    #for negative numbers
    if(x < 0):
        sign_change = -1
        x = x * sign_change

    minimum = 2 ** 31
    while(x > 0):
        number = x % 10
        result = result * 10 + number
        if result * sign_change  <= -minimum or  result* sign_change >= minimum-1:
            return 0
        x = x // 10

    return result * sign_change
    


if __name__ == '__main__':
    reverse(369)