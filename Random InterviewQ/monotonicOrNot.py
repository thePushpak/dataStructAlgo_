def monotonic(list):
    if len(list) <= 2:
        return "Monotonic"
    
    # increase = sorted(list)
    # decrease = sorted(list, reverse=True)
    
    # if increase == list or decrease == list:
    #     return "Monotonic"
    
    # else:
    #     return "Not a monotonic!"

    increasing = all([list[i]<=list[i+1] for i in range(len(list)-1)])
    
    decreasing = all([list[i]>=list[i+1] for i in range(len(list)-1)])    

    if increasing or decreasing:
        return "Monotonic"
    
    return "Not a Monotonic!"
    
    
print(monotonic([1,3,5,7,9]))