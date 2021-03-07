class Solution:
	List = []
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		pivot = len(nums)
		while True:
			pivot -= 1
			index1 = pivot
			if target - nums[index1] in nums[:index1]:
				index2 = nums[:index1].index(target - nums[index1])
				return [index2, index1]

print(Solution.twoSum([0, 3, 4, 0], 0))
