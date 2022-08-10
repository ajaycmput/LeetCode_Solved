def isMonotonic(nums):
    response = True  # base case, eg if len(nums) == 1
    i = 0
    j = i + 1

    if nums[(len(nums)-1)] >= nums[i]:   # monotone Increasing
        while ( j <= len(nums)-1 ):
            if nums[i] <= nums[j]:
                response = True
                i += 1
                j += 1
            else:
                response = False
                break
    else:
        while ( j <= len(nums)-1  ):
            if nums[i] >= nums[j]:
                response = True
                i += 1
                j += 1
            else:
                response = False
                break

    return response