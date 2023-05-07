'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
'''

from typing import List

# O(nm)
def longestCommonPrefix(strs: List[str]) -> str:
    if not strs:
        return ''
    
    m = min(strs)
    M = max(strs)
    result =''
    
    for i in range(len(m)):
        if m[i] == M[i]:
            result += m[i]
        else:
            break
        
    return result
    
# O(nm)
# def longestCommonPrefix(strs: List[str]) -> str:
#     if not strs:
#         return ''
    
#     min_len = min([len(s) for s in strs])
    
#     for i in range( min_len):
#         if len(set([s[i] for s in strs])) > 1:
#             return strs[0][:i]
#     return strs[0][:min_len]
        

print(longestCommonPrefix(["flower","flow","flight"]))