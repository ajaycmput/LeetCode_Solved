"""
    Name: Nnamdi Ajoku
    Language: Python3

    Description: Given an integer n, return an array ans of length n + 1
    such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary 
    representation of i.

    Problem Approach: Runtime O(n^2). Working on Optimizing it. I used a Recursive Approach
    to generate the bits. after that I count the bits.

    code beats just 5%. Pretty slow.

"""
class Solution:
    def countBits(self, n: int) -> List[int]:
        i = 0
        res = []
        while ( i <= n ):
            ans = self.generate_bits(i, "")
            counter = 0
            for j in range(len(ans)):
                if ans[j] == "1":
                    counter += 1
            res.append(counter)
            i += 1

        return res

    def generate_bits(self, num, bits):
        # calculate divisor
        divisor = num // 2
        rem = num % 2
        bits = bits + str(rem)  # bits is in string


        # convert back to int


        # base case
        if divisor == 0:
            return bits

        else:
           return self.generate_bits(divisor, bits)