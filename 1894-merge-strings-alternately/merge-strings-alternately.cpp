class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        
        // First, find the max value
        int len1{static_cast<int>(word1.size())};
        int len2{static_cast<int>(word2.size())};
        int max{std::max(len1, len2)};

        // Create an empty new string
        std::string newString{};

        // Loop through each vector
        for (int i = 0; i < max; i++)
        {
            if (i < len1)
            {
                newString.push_back(word1[i]);
            }
            if (i < len2)
            {
                newString.push_back(word2[i]);
            }
        }

        // Return the result
        return newString;
    }
};