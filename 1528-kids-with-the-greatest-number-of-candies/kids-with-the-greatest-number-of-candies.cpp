class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        
        // First, find the kid with the most candies
        int maxCandies = *std::max_element(candies.begin(), candies.end());

        // Initialize an array of booleans to track
        std::vector<bool> result;

        // Now, iterate though the array to see if it will be more than the max
        for (int kids : candies)
        {
            if (kids + extraCandies >= maxCandies)
            {
                result.push_back(true);
            }
            else
            {
                result.push_back(false);
            }
        }

        // Return the result
        return result;
    }
};