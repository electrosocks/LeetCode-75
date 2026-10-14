class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        
        // First, make a write pointer
        int write = 0;

        // Now, cycle though nums
        for (int read = 0; read < nums.size(); read++)
        {
            // If the index is not zero
            if (nums[read] != 0)
            {
                // Then swap it with the write value.
                int temporary = nums[write];
                nums[write] = nums[read];
                nums[read] = temporary;

                // Update right to the next index
                write++;
            }
        }

    }
};