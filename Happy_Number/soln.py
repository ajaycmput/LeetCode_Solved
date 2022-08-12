"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: Write an algorithm to determine if a number n is happy.

    A happy number is a number defined by the following process:

    Starting with any positive integer, replace the number by the sum of the squares of its digits.

    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

    Those numbers for which this process ends in 1 are happy.

    Return true if n is a happy number, and false if not.

    Problem Approach : Improved DP + Memoization
"""
def isHappy(n):
  
    def dfs(n, track):
        # if repetition occurs return False 
        if n in track:
            return track[n]

        # base case

        if n == 1:
            return True

        key = 0

        for i in str(n):
            key = key + pow(int(i),2)

        track[n] = False
        
        return dfs(key, track)
    
    return dfs(n, {})