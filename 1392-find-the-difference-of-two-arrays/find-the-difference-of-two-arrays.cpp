// Create a function that returns the unique values of one vector
vector<int> getUniqueValuesOfVector(vector<int>& vector1, vector<int>& vector2){

    // Create hashmap and add add vector1 in
    unordered_set<int> valuesInVector1;

    // Add values to valuesInVector1
    for (int value : vector1){
        valuesInVector1.insert(value);
    }

    // Compare values in Vector1 to values in Vector2
    unordered_set<int> uniqueValuesInVector2{};
    for (int value : vector2){
        if (valuesInVector1.find(value) == valuesInVector1.end()){
            uniqueValuesInVector2.insert(value);
        }
    }
    return vector<int>(uniqueValuesInVector2.begin(), uniqueValuesInVector2.end());
}

class Solution {
public:
    vector<vector<int>> findDifference(vector<int>& nums1, vector<int>& nums2) {

        return { getUniqueValuesOfVector(nums2, nums1), getUniqueValuesOfVector(nums1, nums2) };        
    }
};