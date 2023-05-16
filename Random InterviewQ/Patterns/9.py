def printTriangle(N):
    for i in range(N):
        for j in range(i+1):
            if (i+j) % 2 == 0:
                print("1", end=" ")
            else:
                print("0", end=" ")
        print()
        
    
printTriangle(6)


'''
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
'''