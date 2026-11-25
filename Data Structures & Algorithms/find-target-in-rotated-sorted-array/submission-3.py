class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        res = -1

        if nums[l] > target:
            prev = -1
            mid = (l + r) // 2
            while prev != mid:
                if nums[mid] == target:
                    res = mid
                    break;
                if nums[mid] > target and nums[mid] > nums[0]:
                    l = mid
                elif nums[mid] > target and nums[mid] < nums[0]:
                    r = mid
                elif nums[mid] < target:
                    l = mid
                prev = mid
                mid = (l + r + 1) // 2
        elif nums[l] < target:
            prev = -1
            mid = (l + r) // 2
            while prev != mid:
                print('m', mid)
                if nums[mid] == target:
                    res = mid
                    break;
                if nums[mid] > target and nums[mid] > nums[0]:
                    r = mid
                    print('1')
                elif nums[mid] < target and nums[mid] >= nums[0]:
                    l = mid
                    print('2')
                elif nums[mid] < target:
                    r = mid
                    print('3')
                prev = mid
                mid = (l + r + 1) // 2
        else:
            return 0
            
        return res