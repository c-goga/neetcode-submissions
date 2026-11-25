class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        length = len(nums)
        for i in range(length):
            number = nums.pop()
            if (number in nums):
                return True
        return False