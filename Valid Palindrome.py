"""
Question link : https://leetcode.com/problems/valid-palindrome
"""

"""
My Solution: 

import re
class solution:
    def isPalindrome(self,s):
        s = re.sub(r'[\W_]','',s).lower()
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
"""

"""
2nd solution WITHOUT USING "RE" PACKAGE 
"""

'''
class Solution:
    def isPalindrome(s):
        res = ''
        for i in s:
            if i.isalnum():
                res += i.lower()
        left = 0
        right = len(res) - 1

        while left < right:
            if res[left] != res[right]:
                return False
            left += 1
            right -= 1
        return True
'''
