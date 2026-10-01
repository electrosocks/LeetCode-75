class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
        bool uniqueOccurences = true;

        // Create a unordered_map to track occurences
        unordered_map<int, int> occurences;

        // Add occurences to the unordered_map
        for (int values : arr)
        {
            occurences[values]++;
        }

        // Create a set to check occurence uniqueness
        unordered_set<int> occurrencesValues;

        // Add values from unordered map
        for (const auto& [key, values] : occurences)
        {
            if (occurrencesValues.find(values) == occurrencesValues.end())
            {
                occurrencesValues.insert(values);
            }
            else
            {
                uniqueOccurences = false;
            }
        }

        return uniqueOccurences;

    }
};