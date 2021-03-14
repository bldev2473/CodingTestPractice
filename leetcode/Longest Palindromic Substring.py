'''
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case)
'''
from collections import deque

class Solution:
	def longestPalindrome(self, s):
		dq = deque(maxlen=len(s))
		result = ''
		max_len = 0
		for i in range(len(s)):
			dq.clear()
			for j in range(i, len(s)):
				dq.append(s[j])
				dq2list = list(dq)
				dq2str = ''.join(dq2list)
				if self.isPalindrome(dq2str):
					if max_len <= len(dq2str):
						result = dq2str
						max_len = len(dq2str)
					
		return result			
					
	def isPalindrome(self, s):
		return (True if s == s[::-1] else False)

sln = Solution()
print(sln.longestPalindrome('babad'))
print(sln.longestPalindrome('cbbd'))