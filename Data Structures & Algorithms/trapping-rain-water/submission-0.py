class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxLeft, maxRight = 0,0
        count = 0
        while l < r:

            if height[l] < height[r]:
                if height[l] > maxLeft:
                    maxLeft = height[l]
                else:
                    count += maxLeft - height[l]
                l += 1
            else:
                if height[r] > maxRight:
                    maxRight = height[r]
                else:
                    count += maxRight - height[r]
                r -= 1
        return count

        
