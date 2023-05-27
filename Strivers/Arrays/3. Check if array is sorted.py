def arraySortedOrNot(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False
    return True
    
print(arraySortedOrNot([1,4,6,8,9,9,9], 7))