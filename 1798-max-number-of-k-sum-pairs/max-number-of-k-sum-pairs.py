class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:

        # Sort the Array
        nums.sort()

        # Define variables
        lp = 0
        rp = len(nums) - 1
        count = 0

        # Main loop
        while lp < rp:
            
            # Check if values match
            if nums[lp] + nums[rp] == k:
                count += 1
                lp += 1
                rp -= 1
            
            # Check which pointer to move
            elif nums[lp] + nums[rp] > k:
                rp -= 1
            elif nums[lp] + nums[rp] < k:
                lp += 1
            
        # Return results
        return count
            
        