class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        # Sum of available pots
        sum = 0
        
        # Check all Pots
        for i in range(len(flowerbed)):
            # Check if ith pot, i-1th pot, and i+1th pot are empty
            if flowerbed[i] == 0:
                empty_pot_left = (i == 0) or flowerbed[i - 1] == 0
                empty_pot_right = (i == len(flowerbed) - 1)  or flowerbed[i + 1] == 0

                if empty_pot_right and empty_pot_left:
                    sum += 1                # Add to count
                    flowerbed[i] = 1        # Add plant (to ensure we account for new potted plant)
        
        return sum >= n
