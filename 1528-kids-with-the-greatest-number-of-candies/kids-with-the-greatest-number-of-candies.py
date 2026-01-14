class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # Define Result
        result = []

        # Initial for loop
        for i in range(len(candies)):
            # Define result with Extra Candies
            sum = extraCandies + candies[i]
            # Find Max
            maxCandies = max(candies)
            # Check for Comparison
            if sum < maxCandies:
                greatest = False
            else:
                greatest = True
            result.append(greatest)
        return result
                