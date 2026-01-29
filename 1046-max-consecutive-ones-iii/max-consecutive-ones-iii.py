class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # Define variables
        lp = 0
        zerocount = 0
        length = len(nums)
        maxVal = 0

        # Main loop
        for i in range(0, length):
            
            # Check if value in loop is zero, add to count
            if nums[i] == 0:
                zerocount += 1
            
            # Check if zerocount is greater than k
            if zerocount > k:

                # If it is, check if left most value getting left behind is zero and decrease count
                if nums[lp] == 0:
                    zerocount -= 1

                # Move window right
                lp += 1
            
            # Update if value is higher
            if (i - lp + 1) > maxVal:
                maxVal = i - lp + 1

        # Return result
        return maxVal
            

