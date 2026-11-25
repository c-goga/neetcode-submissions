class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = [0] * len(nums)
        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                mult = mult * nums[j]
            l[i] = mult
        return l