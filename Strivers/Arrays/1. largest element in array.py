def largest(arr, n):
    max = arr[0]
    for i in range(1, n):
        if max < arr[i]:  
           max = arr[i]
           
    return max

print(largest([1,23,5,6,4,4], 6))