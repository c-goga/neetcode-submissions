class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        mid = int((l + r) / 2)
        prev = -1
        while nums[mid] != target:
            print('mid', mid)
            if prev == mid:
                return -1
            prev = mid

            if target > nums[mid]:
                l = mid
            else:
                r = mid
            mid = int((l + r) / 2)

        return mid