class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        increment = 0
        length = len(nums)
        for i in range(1, length):
            i = i + increment
            if i >= len(nums):
                break;
            if (nums[i] == nums[i-1]):
                nums.remove(nums[i])
                increment = increment - 1
        
        return len(nums)