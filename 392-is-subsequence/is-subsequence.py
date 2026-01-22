class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Define variables
        sp = 0
        tp = 0

        # Main loop
        while tp < len(t) and sp < len(s):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)