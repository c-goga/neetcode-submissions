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
        if (zeroCount == 1): # one zero means only one point will have product
            l = [0] * len(nums)
            l[zeroIdx] = product
        elif (zeroCount >= 2): # two or more zeros means all zeroes
            l = [0] * len(nums)
        else: # no zeros means division is good
            l = [product] * len(nums)
            for i in range(len(nums)):
                l[i] = int(l[i] / nums[i])
        return l

