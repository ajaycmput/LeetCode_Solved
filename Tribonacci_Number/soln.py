"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: The Tribonacci sequence Tn is defined as follows: 

    T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

    Given n, return the value of Tn.

    Problem Approach: Improved Recurson + Memoization - Fast Dynamic Programming

"""

def tribonacci(n):
    
    def dfs(n, track):
        
        # memoization + 
        if n in track:
            return track[n]
        
        # base case
        
        if n == 1:
            return 1
        elif n <= 0:
            return 0
        
        # recursion
        
        track[n]  = dfs(n-1,track) + dfs(n-2, track) + dfs(n-3, track)
        
        return track[n]
    
    
    return dfs(n,{})