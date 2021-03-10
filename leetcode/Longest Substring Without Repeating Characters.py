from collections import namedtuple
LLS = namedtuple('LLS', ['str', 'len', 'result'])

class Solution:
    def __init__(self):
        self.memoization_dict = {}
    
    def lengthOfLongestSubstring(self, s):
    	for i in range(1, len(s) + 1):
    		for j in range(len(s) + 1 - i):
    			print(s)
    			print('solve: ', self.solve(s[j:j + i]))
    	print(self.memoization_dict)
    	return max(self.memoization_dict.values())
    def solve(self, s):
    	if self.memoization_dict.get(s) is not None:
    		self.memoization_dict.get(s)
    		return LLS(s, len(s), True)
    	if len(s) == 1:
    		self.memoization_dict[s] = 1
    		return LLS(s, len(s), True)
    	else:
    		if len(set(s)) == len(s):
    			self.memoization_dict[s] = len(s)
    			return LLS(s, len(s), True)
    		else:
    			return LLS(s, len(s), False)
    				
sln = Solution()
print(sln.lengthOfLongestSubstring('bbbbbbb'))
print(sln.lengthOfLongestSubstring('abcabcbb'))
print(sln.lengthOfLongestSubstring('pwwkew'))
