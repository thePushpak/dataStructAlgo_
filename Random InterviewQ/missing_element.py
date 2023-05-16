def missing_element_lists(A, B):
    sum_a = sum(A)
    sum_b = sum(B)
    
    missing_element = sum_a-sum_b
    if missing_element == 0:
        return "No missing elements!"
    return missing_element


print(missing_element_lists([1,2,34,5,6],[1,2,5,6,34]))