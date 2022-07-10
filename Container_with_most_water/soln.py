"""
    Name: Nnamdi Ajoku

    Language: Python
    
    Description: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a container, such that the container contains the most water.

    Return the maximum amount of water a container can store.
"""
def maxArea(self, height: List[int]) -> int:
    max = 0
    lr = 0
    rp = len(height) - 1
    while(lr < rp):
        length = rp - lr
        min_height = min(height[lr], height[rp])
        if height[lr] < height[rp]:
            area = length * height[lr]
            if area > max:
                max = area
                lr = lr + 1
            else:
                lr = lr + 1
        else:
            area = length * min_height
            if area > max:
                max = area
                rp = rp -1
            else:
                rp = rp -1
    return max

if __name__ =='__main__':
    maxArea([1,8,6,2,5,4,8,3,7])