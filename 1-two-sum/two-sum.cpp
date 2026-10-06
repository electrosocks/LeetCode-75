class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            int hashComplement = target - nums[i];
            if (hash.find(hashComplement) != hash.end())
            {
                return{hash[hashComplement], i};
            }
            hash[nums[i]] = i;
        }
        return {};
    }
};