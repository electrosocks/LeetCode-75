class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        # Define variables
        vowels = 'aeiouAEIOU'
        length = len(s)
        count = 0

        # Initial loop
        for i in range(0, k):
            if s[i] in vowels:
                count += 1
        
        MaxVowel = count

        # Main loop
        for i in range(k, length):

            # Remove first letter
            if s[i - k] in vowels:
                count -= 1

            # Add last letter
            if s[i] in vowels:
                count += 1
            
            # Check if larger
            if count > MaxVowel:
                MaxVowel = count

        return MaxVowel