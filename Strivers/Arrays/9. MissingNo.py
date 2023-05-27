def missingNumber(nums):
    n = len(nums)
    # set_nums = set(nums)
    
    # for i in range(n+1):
    #     if i not in set_nums:
    #         return i
        
    # arithmatic sequence solution
    expected_sum = n * (n+1) // 2 
    
    actual_sum = sum(nums)
    missing = expected_sum - actual_sum
    
    return missing
    
print(missingNumber([0, 1]))
