def singleNumber(nums):
    result = 0
    
    for num in nums:
        result ^= num
    
    return result
    
    
print(singleNumber([1,1,4,4,3]))