class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # Length 
        len1 = len(str1)
        len2 = len(str2)

        # Valid checker
        def valid(k):
            if len1 % k != len2 % k:                                        # Is there a common divisor for length?
                return False
            n1 = len1 // k                                                  # What is the length when divided?
            n2 = len2 // k
            candidate = str1[:k]                                            # Define the candidate
            return str1 == candidate * n1 and str2 == candidate * n2        # Return boolean of str1 == candidate * n1
        
        for i in range(min(len1, len2), 0, -1):
            if valid(i):
                return str1[:i]
        return ""
            



