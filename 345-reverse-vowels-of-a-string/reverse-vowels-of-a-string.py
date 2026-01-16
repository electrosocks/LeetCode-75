class Solution:
    def reverseVowels(self, s: str) -> str:
        
        # Convert to a list
        word = list(s)

        # Define Vowels
        vowels = 'aeiouAEIOU'

        # Define start and end points
        start = 0
        end = len(s) - 1

        # Iterate through each letter
        while start < end:

            # Iterate the start value right until finding a vowel
            while start < end and vowels.find(word[start]) == -1:
                start += 1
            
            # Iterate the end value left until finding a vowel
            while start < end and vowels.find(word[end]) == -1:
                end -= 1
            
            # Now, swap the characters
            word[start], word[end] = word[end], word[start]

            # Update to not double swap letters before the next loop
            start += 1
            end -= 1
        
        # Final result
        result = "".join(word)
        return result