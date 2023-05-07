'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3.
'''


def romanToInt(s: str) -> int:
    roman_to_int_dict = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                }
    result = 0
    str_length = len(s)
    for c in range(str_length):
        if c < str_length - 1 and  roman_to_int_dict[s[c]] < roman_to_int_dict[s[c+1]]:
            result -= roman_to_int_dict[s[c]]
        else:
            result += roman_to_int_dict[s[c]]
    return result


print(romanToInt('IX'))