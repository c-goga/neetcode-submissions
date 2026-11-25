class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        diff = r - l

        maxArea = 0
        while l < r:
            print(heights[l])
            print(heights[r])
            print()
            smallestHeight = 0
            if heights[l] < heights[r]:
                smallestHeight = heights[l]
                l += 1
            else:
                smallestHeight = heights[r]
                r -= 1
            if smallestHeight * diff > maxArea:
                maxArea = smallestHeight * diff
            diff = r - l
            # if smallestHeight >= diff:
            #     break
        return maxArea
