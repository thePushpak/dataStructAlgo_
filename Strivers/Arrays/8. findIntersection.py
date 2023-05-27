def findIntersection(arr1, arr2):
    n1 = len(arr1)
    n2 = len(arr2)
    intersection_list = []
    
    i = 0
    j = 0
    
    while i < n1 and j < n2:
        if arr1[i] == arr2[j]:
            intersection_list.append(arr1[i])
            i += 1
            j += 1
            
        elif arr1[i] < arr2[j]:
            i += 1
            
        else: 
            j += 1
            
    return intersection_list


print(findIntersection([1,2,3,4,5,6],[3,4,5]))