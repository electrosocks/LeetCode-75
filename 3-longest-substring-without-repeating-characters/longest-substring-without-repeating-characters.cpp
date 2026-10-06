class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int leftptr = 0;
        int window = 0;
        std::unordered_set<char> currentChars;
        int maxVal = 0;
        
        for (int rightptr = 0; rightptr < s.size(); rightptr++)
        {
            while (currentChars.find(s[rightptr]) != currentChars.end() && leftptr < rightptr)
            {
                currentChars.erase(s[leftptr]);
                leftptr++;
            }
            currentChars.insert(s[rightptr]);

            int window = rightptr - leftptr + 1;
            maxVal = std::max(maxVal, window);
        }

        return maxVal;
    }
};