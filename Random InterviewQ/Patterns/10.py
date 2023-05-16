def printTriangle(N):
    for i in range(N):
        for j in range(i+1):
            print(chr(65+j), end='')
        print()
    
    
printTriangle(6)


'''
A
AB
ABC
ABCD
ABCDE
ABCDEF
'''