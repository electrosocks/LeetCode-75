class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        
        i = 0
        length = len(nums)
        while i < length:          # Main loop

            if nums[i] == 0:                # If the value equals zero

                nums.append(nums[i])        # Append the value to the end
                del nums[i]                 # Delete the value from the list
                length -= 1
            
            else:
                i += 1
