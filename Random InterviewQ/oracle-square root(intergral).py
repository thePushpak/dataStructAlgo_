# bruteforce method (O(n^2))

# def square_root(n):
#     if n == 0:
#         return 0
    
#     i = 1
#     while i*i <= n:
#         i+=1
          
#     return i-1
    
# O(log n)
def square_root(n):
    if n == 0:
        return 0
    
    left, right = 1, n
    
    while left <= right:
        mid = (left + right) // 2
        
        if mid * mid == n:
            return mid
        
        elif mid * mid < n:
            left = mid + 1
            
        else:
            right = mid - 1
            
    return right
    
print(square_root(18))