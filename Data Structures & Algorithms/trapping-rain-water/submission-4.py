class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        # Precompute the maximum height to the left and right of each bar
        left_max = [0] * len(height)
        right_max = [0] * len(height)
        
        left_max[0] = height[0]
        for i in range(1, len(height)):
            left_max[i] = max(left_max[i - 1], height[i])
            
        right_max[len(height) - 1] = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
            
        totalArea = 0
        # The water above any bar is the minimum of the highest bars to its left and right,
        # minus its own height.
        for i in range(len(height)):
            water = min(left_max[i], right_max[i]) - height[i]
            if water > 0:
                totalArea += water
                
        return totalArea