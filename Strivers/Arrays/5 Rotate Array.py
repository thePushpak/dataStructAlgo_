def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k %= n  # To handle cases where k > n
    
    for _ in range(k):
        nums.insert(0, nums.pop())

print(rotate([1,2,3,4,5,6,7], 3))