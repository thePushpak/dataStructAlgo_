def printTriangle(N):
    for i in range(N):
        # for j in range(i):
        #     print(' ', end='')
        # for j in range(2*(N-i)-1):
        #     print('*', end='')
        # print()    
        print((' '*i) + ('*'*(2*(N-i)-1)))
        
        
printTriangle(6)

'''
***********
 *********
  *******
   *****
    ***
     *
'''