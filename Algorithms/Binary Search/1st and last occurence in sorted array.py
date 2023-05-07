def index(arr, target):
    if len(arr) == 0:
        return -1
        
    start = 0
    end = len(arr)-1
    first_pos = -1
    last_pos = -1
    
    while start <= end:
        mid = start + (end-start) // 2
        
        if arr[mid] == target:
            first_pos = mid
            end = mid - 1
        
        elif arr[mid] < target:
            start = mid + 1
            
        else:
            end = mid - 1
            
    start = 0
    end = len(arr)-1
    
    while start <= end:
        mid = start + (end-start) // 2
        
        if arr[mid] == target:
            last_pos = mid
            start = mid + 1
        
        elif arr[mid] < target:
            start = mid + 1
            
        else:
            end = mid - 1
        
    return (first_pos, last_pos)


print(index([2,3,4,4,4,5,6,7], 4))