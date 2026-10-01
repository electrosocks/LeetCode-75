// Create a function that compares 2 vectors to eachother
vector<int> uniqueValuesInFirstVector(const vector<int>& v1, const vector<int>& v2)
{
    // Create a unordered_map to track
    unordered_set<int> valuesInV2(v2.begin(), v2.end());
    unordered_set<int> uniqueValuesInV1;

    // Compare with values in V1
    for (int value : v1)
    {
        if (valuesInV2.find(value) == valuesInV2.end())
        {
            uniqueValuesInV1.insert(value);
        }
    }

    return vector<int>(uniqueValuesInV1.begin(), uniqueValuesInV1.end());
    }

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {
        return {uniqueValuesInFirstVector(nums1, nums2), uniqueValuesInFirstVector(nums2, nums1)};
    }
};