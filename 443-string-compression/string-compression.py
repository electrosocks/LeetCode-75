class Solution:
    def compress(self, chars: List[str]) -> int:
        
        # Define variables
        s = []
        tally = 0
        length = len(chars)

        # Main loop
        for i in range(length):

            prev = chars[i - 1] if i > 0 else None              # Define previous with edge case
            next = chars[i + 1] if i < length - 1 else None     # Define next with edge case

            tally += 1                                          # Add tally per iteration

            if chars[i] != prev:
                s.append(chars[i])                              # Append if no repeats
            if chars[i] != next:
                if tally > 1:
                    s.extend(list(str(tally)))                  # Append Tally as separate strings
                tally = 0  
        
        # Reset list and print
        for i in range(len(s)):
            chars[i] = s[i]

        # Return results
        return len(s)
