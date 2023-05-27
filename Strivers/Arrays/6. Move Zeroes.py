def MoveZeros(nums):
    if len(nums) < 2:
        return -1
    
    zeroes = nums.count(0) 
    
    nums[:] = [num for num in nums if num != 0]
    nums += [0] * zeroes
    print(nums)
    

MoveZeros([2,23,4,5,0,776,0,77,0,43,2,2])
