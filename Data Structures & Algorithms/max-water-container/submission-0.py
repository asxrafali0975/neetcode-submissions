class Solution:
    def maxArea(self, heights: List[int]) -> int:
        size = len(heights)
        low = 0
        high = size-1
        maxcount  = 0

        while high!=low:
            count = (high-low)*min(heights[low],heights[high])
            maxcount = max(maxcount , count)
            if heights[low]<=heights[high]:
                low+=1
            else:
                high-=1

        return maxcount
        