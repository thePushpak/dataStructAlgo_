'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:
Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.

Example 1:
Input: s = "   -42"
Output: -42
'''

# O(n)
def myAtoi(s: str) -> int:
    sign = 1
    result = 0
    i = 0
    n = len(s)
    
    # skip whitespace and handle sign
    while i < n and s[i] == ' ':
        i += 1
    if i < n and (s[i] == '+' or s[i] == '-'):
        if s[i] == '-':
            sign = -1
        i += 1
    
    # lookup table for digits
    digits = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, 
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
    }
    
    # convert digits to integer
    while i < n and s[i] in digits:
        result = result * 10 + digits[s[i]]
        i += 1
    
    # apply sign and check for overflow
    result = result * sign
    result = max(min(result, 2**31 - 1), -2**31)
    
    return result

print(myAtoi('  -332'))