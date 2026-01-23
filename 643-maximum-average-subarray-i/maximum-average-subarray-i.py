class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        # Define variables
        length = len(nums)
        windowSum = sum(nums[:k])
        maxSum = windowSum

        # Main loop
        for i in range(k, length):

            # Update new window sum
            windowSum += nums[i]
            windowSum -= nums[i-k]

            # Update largest sum
            if windowSum > maxSum:
                maxSum = windowSum

        return maxSum / k