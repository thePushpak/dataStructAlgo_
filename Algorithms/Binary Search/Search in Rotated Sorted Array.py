from typing import List

def search_rotated_sorted_array(nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = start + (end-start) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[end]:
                if nums[mid] < target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
            else:
                if nums[start] <= target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
        return -1

print(search_rotated_sorted_array([4,5,6,7,0,1,2], 0))