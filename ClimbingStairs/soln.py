"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you
    
    climb to the top?

    Problem Approach: By drawing the recursion tree, this probelm is similar to UniquePaths.

    It keeps track of repeating nodes in a dictionary and simply re-uses each node if it repeats

    again. If the stair goes above the top(n), return 0 else if stair reaches the top, return 1. 

    From my recursion tree, going left = + 1 step, going right = + 2 steps.

"""
def climbStairs(n):  
    def dfs(key, track):

        if key in track:
            return track[key]

        # base cases

        # if the top of stairs is reached (n),  return 1 (one way)

        if key == n:
            return 1
        elif key > n:
            return 0

        #               adding 1 step    +    addding 2 steps
        track[key] = dfs(key + 1, track) + dfs(key + 2, track)

        return track[key]


    return dfs(0, {})
