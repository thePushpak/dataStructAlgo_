def print2largest(arr, n):
    if n < 2:
        return -1
        
    largest = max(arr)
    second_largest = -1
    
    for i in range(1, n):
        if largest != arr[i] and arr[i] > second_largest:
            second_largest = arr[i]
        
    
    return second_largest


print(print2largest([1,56,73,888,2245,33,567], 7))