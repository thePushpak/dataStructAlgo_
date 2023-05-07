# using bruteforce method 1
# def index(list, n):
#     for i, num in enumerate(list):
#         if num == n:
#             return i
        
#     return -1

# using bruteforce method 2
# def index(list, n):
#     for i in range(len(list)):
#         if list[i] == n:
#             return i
#     return -1

# using Binary search 
# def index(list, n):
#     start = 0
#     end = len(list)-1
    
#     while start <= end:
#         mid = start + (end-start)//2
#         if list[mid] == n:
#             return mid
        
#         elif n > list[mid]:
#             start = mid + 1
        
#         else:
#             end = mid - 1
    
#     return -1

# print(index([1,2,3,4,5], 4))


# # for reverse array
# def index(list, n):
#     start = 0
#     end = len(list)-1
    
#     while start <= end:
#         mid = start + (end-start)//2
#         if list[mid] == n:
#             return mid
        
#         elif n > list[mid]:
#             end  = mid - 1
        
#         else:
#             start = mid + 1
    
#     return -1

# print(index([9,8,7,6,5,4,3,2,1], 7))


# sorted array ascending or descending not known 
def index(list, n):
    if len(list) == 0:
        return -1
    
    start = 0
    end = len(list)-1
    
    # ascending
    if list[0] < list[1]: 
        while start <= end:
            mid = start + (end-start)//2
            if list[mid] == n:
                return mid
            
            elif n > list[mid]:
                start = mid + 1
            
            else:
                end = mid - 1
    # descending
    else: 
        while start <= end:
            mid = start + (end-start)//2
            if list[mid] == n:
                return mid
            
            elif n > list[mid]:
                end  = mid - 1
            
            else:
                start = mid + 1
    
    return -1
    

print(index([9,8,7,6,5,4,3,2,1], 7))
