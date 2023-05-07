'''
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''

def longestPalindrome(s: str) -> str:
    reverse=''
    for i in s:
        reverse = i + reverse
        print(reverse)
    reverse = int(reverse)
    return reverse

print(longestPalindrome('123'))