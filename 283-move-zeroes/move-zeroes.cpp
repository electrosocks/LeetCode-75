class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        // First, make a iterator for the very left
        int leftIterator{0};

        // Loop through all elements
        for (int rightIterator{0}; rightIterator < nums.size(); rightIterator++)
        {
            // If the right iterator does not equals zero
            if (nums[rightIterator] != 0)
            {
                // Move it left
                swap(nums[rightIterator], nums[leftIterator]);

                // Update the left iterator location only if it now conains a real value
                leftIterator++;
            }
        }

    }
};