class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # Define variables
        lp = 0
        length = len(nums)
        zerocount = 0
        maxSize = 0

        # Main loop
        for i in range(0, length):

            # If nums[i] = 1, do nothing

            # If nums[i] = 0, add to zerocount
            if nums[i] == 0:
                zerocount += 1

            # Check zero count number
            while zerocount > 1:

                # Check if end cap is zero
                if nums[lp] == 0:

                    # Lower zero count
                    zerocount -= 1
                
                # Move pointer
                lp += 1

            if zerocount < 1:
                delete = 1
            else:
                delete = zerocount

            # Update maxSize
            if maxSize < i - lp + 1 - delete:
                maxSize = i - lp + 1 - delete

        # Return Result
        return maxSize
            