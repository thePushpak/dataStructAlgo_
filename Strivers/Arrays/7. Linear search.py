def searchInSorted(arr, N, K):
    if N < 1:
        return -1
    
    for i in range(N):
        if arr[i] == K:
            return 1
        
    return -1


print(searchInSorted([1,2,4,5,6], 5, 3))