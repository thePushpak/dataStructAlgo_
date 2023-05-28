'''
Given a string s, return the longest palindromic substring in s.
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
'''

def longestPalindrome(s):
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len, start, end = 1, 0, 0
        for i in range(n-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j - i + 1 > max_len:
                        max_len = j - i + 1
                        start, end = i, j
        return s[start:end+1]


print(longestPalindrome("cbbd"))