'''
Given a string s, find the length of the longest 
substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
'''
# sliding window
def lengthOfLongestSubstring(s: str) -> int:
    used = {}
    start, longest = 0, 0
    for i, c in enumerate(s):
        if c in used and start <= used[c]:
            start = used[c] + 1
        else:
            longest = max(longest, i - start + 1)
        used[c] = i
    return longest


s='abcabb'
print(lengthOfLongestSubstring(s))