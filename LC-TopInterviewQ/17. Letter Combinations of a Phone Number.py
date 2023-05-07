'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
'''

from typing import List

def letterCombinations(digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz' 
        }
        
        def backtrack(combination, remaining_digits):
            if not remaining_digits:
                result.append(combination)
                
            else:
                for letter in mapping[remaining_digits[0]]:
                    backtrack(combination+letter , remaining_digits[1:])
        
        
        result = []
        backtrack('', digits)
        return result
    

print(letterCombinations('233'))
