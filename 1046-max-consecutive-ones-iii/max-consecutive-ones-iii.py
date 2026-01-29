class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        # Define variables
        maxNum = 0
        length = len(nums)
        tally = 0
        lp = 0
        rp = 0

        for i in range(0, length):
            if nums[i] == 0:
                tally += 1
            if tally > k:
                if nums[lp] == 0:
                    tally -= 1
                lp += 1


            if (i - lp + 1) > maxNum:
                maxNum = i - lp + 1
        
        return maxNum

            

