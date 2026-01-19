class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Define variables
        length = len(nums)
        result = [1] * length
        left = 1
        right = 1
        left_values = [1] * length
        right_values = [1] * length

        # Main loop
        for i in range(length):

            # Multiply values left
            left_values[i] = left           # Store FIRST for edge cases
            left *= nums[i]                 # Then update

            # Multiply values right
            right_values[length - i - 1] = right
            right *= nums[length - i - 1]

        for i in range(length):
            result[i] = left_values[i] * right_values[i]

        return result