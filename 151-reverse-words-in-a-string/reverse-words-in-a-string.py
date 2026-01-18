class Solution:
    def reverseWords(self, s: str) -> str:

        # Separate string into a list of words
        words_list = s.split()

        # Variables for constant
        start = 0
        end = len(words_list) - 1

        # Iterate through length of word
        for i in range(len(s)):
            if start < end:
                words_list[start], words_list[end] = words_list[end], words_list[start]
                start += 1
                end -= 1
        
        # Return the result
        result = " ".join(words_list)
        return result

