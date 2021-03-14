'''
#Time Limit Exceeded

from collections import namedtuple
LLS = namedtuple('LLS', ['str', 'len', 'result'])

class Solution:
	def __init__(self):
		self.memoization_dict = {}

	def lengthOfLongestSubstring(self, s):
		if len(s) <= 1:
			return len(s)
		for i in range(1, len(s) + 1):
			for j in range(len(s) + 1 - i):
				#print(s)
				#print('solve: ', self.solve(s[j:j + i]))
				self.solve(s[j:j + i])
		#print(self.memoization_dict)
		return max(self.memoization_dict.values())

	def solve(self, s):
		if self.memoization_dict.get(s) is not None:
			self.memoization_dict.get(s)
			return LLS(s, len(s), True)
		if len(s) <= 1:
			self.memoization_dict[s] = len(s)
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
print(sln.lengthOfLongestSubstring(''))
'''

#Success
#Runtime: 240 ms, faster than 19.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
#Memory Usage: 14.4 MB, less than 27.85% of Python3 online submissions for Longest Substring Without Repeating Characters.

from collections import deque

class Solution:
    def __init__(self):
        self.memoization_dict = {}

    def lengthOfLongestSubstring(self, s):
        dq = deque(maxlen=len(s))
        if len(s) <= 1:
            return len(s)
        for i in range(0, len(s)):
            dq.append(s[i]);
            # print(dq)
            if self.solve(dq) is not True:
                dq.popleft()
                continue
            else:
                continue
        return max(self.memoization_dict.values())

    def solve(self, dq):
        m_list = ''.join(list(dq))
        if self.memoization_dict.get(m_list) is not None:
            return True
        if len(m_list) <= 1:
            self.memoization_dict[m_list] = len(m_list)
            return True
        else:
            if len(set(m_list)) == len(m_list):
                self.memoization_dict[m_list] = len(m_list)
                return True
            else:
                return False

sln = Solution()
print(sln.lengthOfLongestSubstring('bbbbbbb'))
print(sln.lengthOfLongestSubstring('abcabcbb'))
print(sln.lengthOfLongestSubstring('pwwkew'))
print(sln.lengthOfLongestSubstring(''))
