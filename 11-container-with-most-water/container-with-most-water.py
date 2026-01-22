class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # Define variables
        maxVolume = 0
        lp = 0
        rp = len(height) - 1

        while lp < rp:
            volume = min(height[lp], height[rp]) * (rp - lp)
            if volume > maxVolume:
                maxVolume = volume
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1

        return maxVolume
            