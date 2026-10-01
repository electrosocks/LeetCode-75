class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
        // We can use a hashmap to track occurences
        unordered_map<int, int> numberFrequencies;

        // Put all values in this map
        for (int value : arr)
        {
            numberFrequencies[value]++;
        }

        // We can use a unordered_set to track duplicates
        unordered_set<int> uniqueness;

        // Check values in unordered_map;
        for (const auto& [key, value] : numberFrequencies)
        {
            if (uniqueness.find(value) == uniqueness.end())
            {
                uniqueness.insert(value);
            }
            else
            {
                return false;
            }
        }

        return true;
    }
};