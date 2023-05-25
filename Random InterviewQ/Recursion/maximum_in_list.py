def find_maximum(list_of_numbers):
    if len(list_of_numbers) == 1:
        return list_of_numbers[0]
    
    mid = len(list_of_numbers) // 2
    
    left_max = find_maximum(list_of_numbers[:mid])
    right_max = find_maximum(list_of_numbers[mid:])
    
    if left_max > right_max:
        return left_max
    return right_max

list_of_numbers = [1, 5, 3, 67, 2,23,5,67,33,24,67,67,34,65]
print(find_maximum(list_of_numbers))
# Prints 67