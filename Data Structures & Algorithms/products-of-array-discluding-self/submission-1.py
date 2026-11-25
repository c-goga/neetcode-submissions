class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeroCount = 0
        zeroIdx = -1
        for i in range(len(nums)):
            if (nums[i] == 0):
                zeroCount += 1
                zeroIdx = i
                continue
            product *= nums[i]
        if (zeroCount == 1):
            l = [0] * len(nums)
            l[zeroIdx] = product
        elif (zeroCount >= 2):
            l = [0] * len(nums)
        else:
            l = [product] * len(nums)
            for i in range(len(nums)):
                if (nums[i] != 0):
                    l[i] = int(l[i] / nums[i])
        return l

