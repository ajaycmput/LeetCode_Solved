/*
    Name: Nnamdi Ajoku

    Language: Javascript

    Description: There is a robot on an m x n grid. The robot is initially

    located at the top-left corner (i.e., grid[0][0]). The robot tries to 

    move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot 

    can only move either down or right at any point in time.

    Given the two integers m and n, return the number of possible unique paths

    that the robot can take to reach the bottom-right corner.

    The test cases are generated so that the answer will be less than or equal to

    2 * 109.


    DISCLAIMER: This problem is best solved with recursion(tree). Tree is Optimized by ensuring that any repeating
                key is immediately returned and not stroed in the set.

*/
const uniquePaths = (m, n, track = {}) => {
    
    const key = m + ',' + n;  // I had a problem executing this line with python dictionary and c++ unordered map.

    if (key in track) return track[key];

    // base cases

    // if there is no row or column, we have no where to go to. Hence return 0
    if ( m == 0 || n == 0) return 0;

    // we only have one option to go to when there is 1 row and 1 column
    else if ( m == 1 && n == 1) return 1;


    //                 going down           +    going right
    track[key] = uniquePaths(m-1, n, track) + uniquePaths(m, n-1, track); 

    return track[key];
    
};