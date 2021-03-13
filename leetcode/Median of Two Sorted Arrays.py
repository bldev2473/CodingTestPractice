'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:

Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:

Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:

Input: nums1 = [2], nums2 = []
Output: 2.00000
 
Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

Follow up: The overall run time complexity should be O(log (m+n)).
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
    	m_list = nums1 + nums2
    	m_list.sort()
    	print(m_list)
    	m_len = len(m_list)
    	
    	result = sum(m_list[int(((m_len / 2) - 1)):int(m_len / 2) + 1]) / 2 if m_len % 2 == 0 else m_list[m_len // 2]
    	
    	return result
    	
sln = Solution()
sln.findMedianSortedArrays([1], [2, 3])
sln.findMedianSortedArrays([1, 2], [3, 4])
sln.findMedianSortedArrays([1, 3], [2, 7])
sln.findMedianSortedArrays([], [1])