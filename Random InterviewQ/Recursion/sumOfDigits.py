def sumOfDigits(num):
    if num == 0:
        return 0
    
    # else:
    #     return int(num%10) + sumOfDigits(int(num/10))
    sum = 0
    while num > 0:
        sum += num%10
        n //= 10
    return sum

print(sumOfDigits(123))


