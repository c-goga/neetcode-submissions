class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []

        i = 0
        length = len(nums)
        while i < length - 2:
            j = i + 1
            while j < length - 1:
                k = j + 1
                while k < length:
                    if nums[i] + nums[j] + nums[k] == 0:
                        if sorted([nums[i], nums[j], nums[k]]) not in res:
                            res.append(sorted([nums[i], nums[j], nums[k]]))
                    k += 1
                j += 1
            i += 1


        return res