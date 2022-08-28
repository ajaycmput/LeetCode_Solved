"""
    Name: Nnamdi Ajoku
    Language: Python

    Description: A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost
    
    column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting 
    
    from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

    Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.


    PROBLEM APPROACH: To  solve this problem, the two main data structures needed is a list and a dictionary. Starting with the topmost mat[0][0]

    section, we move by increasing the columns by 1. 

    Two loops are needed, the first one is to get to a column, the second one is to move diagonally in that column. When moving diagonaaly, i increase
    
    the row and column by 1 , and store its index and value as a key-value pair in a dictionary.

    < This is t ensure I keep track of the indices >. I stored the values in a dynamically changing ( temporary ) list and looped through the dictionary, with the original 

    index of the matrix and simply appended the increasing index of the list as its value: mat[key1][key2] = track[key1,key2]

    I did the same thing to the leftmost side, buy increasing the row from top to bottom.


"""

def diagonalSort(mat):
    # topmost
    
    vertical  = 0
    while( vertical <= len(mat[0])-1):
        row, col = 0, vertical
        temp, track = [], {}
        
        while ( row <= len(mat)-1) and ( col <= len(mat[0])-1):
            track[row,col] = mat[row][col]
            temp.append(mat[row][col])
            col += 1
            row += 1
           
        temp.sort()
        index = 0
        for key in track.keys():
            track[key] = temp[index]
            index += 1
            
        for key1,key2 in track.keys():
            mat[key1][key2] = track[key1 , key2]
            
        vertical+= 1
        
    # leftmost
    
    horizontal = 0
    while(  horizontal <= len(mat)-1):
        col, row = 0, horizontal
        temp, track = [], {}
        
        while ( row <= len(mat)-1) and ( col <= len(mat[0])-1):
            track[row,col] = mat[row][col]
            temp.append(mat[row][col])
            col += 1
            row += 1
            
        temp.sort()
        index = 0
        for key in track.keys():
            track[key] = temp[index]
            index += 1
            
        for key1,key2 in track.keys():
            mat[key1][key2] = track[key1 , key2]
            
        horizontal+= 1
        
    
    return mat # return the matrix