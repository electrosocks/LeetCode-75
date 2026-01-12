class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Define variables
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        # Main loop
        while i < m or j < n:
            if i < m:
                result += word1[i]
            if j < n:
                result += word2[i]
            i += 1
            j += 1
        
        # Format Results
        # This function works by setting a separator (or lack thereof)
        # and then joining all parts with one another. 
        result = "".join(result)

        # Return result
        return result
