def removeDuplicates(nums):
    nums[:] = sorted(set(nums))
    return len(nums)


print(removeDuplicates([1,233,555,555,67,8,8]))