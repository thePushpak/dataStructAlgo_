def removeOuterParentheses(S):
    stack = []
    result = []
    
    for char in S:
        if char == '(':
            if stack:
                result.append(char)
            stack.append(char)
            
        else: 
            stack.pop()
            if stack:
                result.append(char)
        
    return ''.join(result)


print(removeOuterParentheses("(()())(())(()(()))"))
    
     