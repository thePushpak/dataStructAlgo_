def printTriangle(N):
    for i in range(N):
        for j in range(N-i):
            print(chr(65+j), end='')
        print()
    
printTriangle(6)


'''
ABCDEF
ABCDE
ABCD
ABC
AB
A
'''