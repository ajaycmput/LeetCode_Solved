"""
    Name: Nnamdi Ajoku
    Language: Python3

    Description: Alice and Bob take turns playing a game, with Alice starting first.

    Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

    Choosing any x with 0 < x < n and n % x == 0. Replacing the number n on the chalkboard with n - x.

    Also, if a player cannot make a move, they lose the game.

    Return true if and only if Alice wins the game, assuming both players play optimally.


    PROBLEM APPROACH: The best way to soolve this problem is through a recursive approach. By sketching the recursion tree
    you get a base case whereby when n ==1 and the turn is even then It was Bob's turn else Alice's turn.

    if the number picked is not divisible by 2, simply jump to the next one.



"""
def divisorGame(self, n: int) -> bool:
    def dfs(n, i, turn):
        # while anyone picks a num less than n
        while( 0 < i < n ):
            n = n - i
            # base case(s)
            # if its Alice's turn
            if  n ==1 and turn % 2 != 0:
                return True
            # if its Bob's turn
            elif n ==1 and turn %2 == 0:
                return False
            else:
                if n % i == 0:
                    turn += 1
                    # run recursive approach
                    return dfs(n, i , turn)
                    # else if number picked is not dividible by 2, go to the next number and check
                else:
                    i += 1
    # return base case
    return dfs(n, 1, 1)