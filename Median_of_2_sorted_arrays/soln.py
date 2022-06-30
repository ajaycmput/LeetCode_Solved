"""
    Name: Nnamdi Ajoku
    Language: Python

"""

import math
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        for i in nums2:
            nums1.append(i)

        nums1.sort()  #sort array

        median1 = 0
        median2 = 0
        median = 0


        length = len(nums1)
        # get the marker
        marker = math.floor(len(nums1)/2)

        # check if its an odd number
        j = 0
        if (length % 2) != 0:
            while( j < length):
                if j == marker:
                    median1= median1 + nums1[j]
                    median = median1
                    break
                else:
                    j+=1
        # if its an even number
        if (length % 2 ) == 0:
            while( j < length):
                if j == marker:
                    median1 = median1 + nums1[j-1]
                    median2 = median2 + (nums1[j])
                    median = float((median1 + median2)/2)
                    break
                else:
                    j+=1
    
        return median