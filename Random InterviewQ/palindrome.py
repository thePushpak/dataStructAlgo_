def palindrome(num):
    rev = 0
    n = num
    while num > 0:
        rev = rev*10 + num %10
        num //= 10 
        
    return rev == n
    

print(palindrome(121))