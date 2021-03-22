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

'''
#Time Limit Exceeded

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
print(sln.longestPalindrome('abbcccbbbcaaccbababcbcabca'))
print(sln.longestPalindrome('"rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip"'))
'''

'''
#Time Limit Exceeded

class Solution:
	def __init__(self):
		self.result = ''
		self.memo_dict = {}
		
	def longestPalindrome(self, s):
		self.memo_dict = {}
		if self.isPalindrome(s):
			return s
		else:
			self.recursive(s, 'right')
			self.recursive(s, 'left')
		
		result_dict = dict(filter(lambda elem: elem[1] == True, self.memo_dict.items()))
		result_dict = list(result_dict.keys())
		result_dict.sort(key=len, reverse=True)
		print(result_dict)
		return result_dict[0]
		
	def recursive(self, s, flag):
		if len(s) == 1:
			self.memo_dict[s] = True
			return
		
		if flag == 'right':
			s = s[:len(s) - 1]
			if self.memo_dict.get(s) is None:
				self.memo_dict[s] = self.isPalindrome(s)
			self.recursive(s, 'right')
			self.recursive(s, 'left')
		else:
			s = s[1:]
			if self.memo_dict.get(s) is None:
				self.memo_dict[s] = self.isPalindrome(s)
			self.recursive(s, 'left')
			self.recursive(s, 'right')
					
	def isPalindrome(self, s):
		return (True if s == s[::-1] else False)

sln = Solution()
print(sln.longestPalindrome('babad'))
print(sln.longestPalindrome('cbbd'))
print(sln.longestPalindrome('a'))
print(sln.longestPalindrome('ac'))
'''

'''
# RecursionError: maximum recursion depth exceeded

class Solution:
	def __init__(self):
		self.result = ''
		self.memo_dict = {}
		
	def longestPalindrome(self, s):
		if self.isPalindrome(s):
			return s
		else:
			self.recursive(s, 'right')
			self.recursive(s, 'left')
		
		result_dict = self.memo_dict
		result_dict = dict(filter(lambda elem: elem[1] == True, result_dict.items()))
		
		result_list = [key for key in result_dict]
		result_list.sort(reverse=True, key=len)
		return result_list[0]
		
	def recursive(self, s, flag):
		if len(s) == 1:
			print('break')
			self.memo_dict[s] = True
			return
		
		if flag == 'right':
			m_str = s[:len(s) - 1]
			print(m_str)
			if self.memo_dict.get(m_str) is None:
				if self.isPalindrome(m_str):
					self.memo_dict[m_str] = True
					
				else:
					self.memo_dict[m_str] = False
					
				self.recursive(m_str, 'right')
				self.recursive(m_str, 'left')
			else:
				return
		else:
			m_str = s[1:]
			print(m_str)
			if self.memo_dict.get(m_str) is None:
				if self.isPalindrome(m_str):
					self.memo_dict[m_str] = True
					
				else:
					self.memo_dict[m_str] = False
					
				self.recursive(m_str, 'right')
				self.recursive(m_str, 'left')
			else:
				return
					
	def isPalindrome(self, s):
		return (True if s == s[::-1] else False)

sln = Solution()
#print(sln.longestPalindrome('babad'))
#print(sln.longestPalindrome('cbbd'))
#print(sln.longestPalindrome('a'))
#print(sln.longestPalindrome('ac'))
#print(sln.longestPalindrome('abbcccbbbcaaccbababcbcabca'))
print(sln.longestPalindrome('esbtzjaaijqkgmtaajpsdfiqtvxsgfvijpxrvxgfumsuprzlyvhclgkhccmcnquukivlpnjlfteljvykbddtrpmxzcrdqinsnlsteonhcegtkoszzonkwjevlasgjlcquzuhdmmkhfniozhuphcfkeobturbuoefhmtgcvhlsezvkpgfebbdbhiuwdcftenihseorykdguoqotqyscwymtjejpdzqepjkadtftzwebxwyuqwyeegwxhroaaymusddwnjkvsvrwwsmolmidoybsotaqufhepinkkxicvzrgbgsarmizugbvtzfxghkhthzpuetufqvigmyhmlsgfaaqmmlblxbqxpluhaawqkdluwfirfngbhdkjjyfsxglsnakskcbsyafqpwmwmoxjwlhjduayqyzmpkmrjhbqyhongfdxmuwaqgjkcpatgbrqdllbzodnrifvhcfvgbixbwywanivsdjnbrgskyifgvksadvgzzzuogzcukskjxbohofdimkmyqypyuexypwnjlrfpbtkqyngvxjcwvngmilgwbpcsseoywetatfjijsbcekaixvqreelnlmdonknmxerjjhvmqiztsgjkijjtcyetuygqgsikxctvpxrqtuhxreidhwcklkkjayvqdzqqapgdqaapefzjfngdvjsiiivnkfimqkkucltgavwlakcfyhnpgmqxgfyjziliyqhugphhjtlllgtlcsibfdktzhcfuallqlonbsgyyvvyarvaxmchtyrtkgekkmhejwvsuumhcfcyncgeqtltfmhtlsfswaqpmwpjwgvksvazhwyrzwhyjjdbphhjcmurdcgtbvpkhbkpirhysrpcrntetacyfvgjivhaxgpqhbjahruuejdmaghoaquhiafjqaionbrjbjksxaezosxqmncejjptcksnoq'))
'''

#Success
#Details 
#Runtime: 9872 ms, faster than 5.01% of Python3 online submissions for Longest Palindromic Substring.
#Memory Usage: 14.3 MB, less than 63.02% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s

        for i in reversed(range(0, len(s) + 1)):
            start_index = -1
            while True:
                start_index += 1
                end_index = start_index + i
                if end_index == len(s) + 1:
                    break

                m_str = s[start_index:end_index]
                if self.isPalindrome(m_str):
                    return m_str

    def isPalindrome(self, s):
        return (True if s == s[::-1] else False)

sln = Solution()
print(sln.longestPalindrome('babad'))
print(sln.longestPalindrome('cbbd'))
print(sln.longestPalindrome('a'))
print(sln.longestPalindrome('ac'))
print(sln.longestPalindrome('bb'))
print(sln.longestPalindrome('abbcccbbbcaaccbababcbcabca'))
