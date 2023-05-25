# First occurence
def index(arr, target):
    if len(arr) == 0:
        return -1
        
    start = 0
    end = len(arr)-1
    res = -1
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] == target:
            res = mid
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return res

# print(index([2,3,4,4,4,5,6,7], 4))
# last occurence
def index(arr, target):
    if len(arr) == 0:
        return -1
        
    start = 0
    end = len(arr)-1
    res = -1
    while start <= end:
        mid = start + (end-start) // 2
        if arr[mid] == target:
            res = mid
            start = mid + 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return res


print(index([2,3,4,4,4,5,6,7], 4))