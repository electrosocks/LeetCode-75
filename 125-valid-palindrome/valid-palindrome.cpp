class Solution {
public:
    bool isPalindrome(string s) {
        int leftPointer = 0;
        int rightPointer = s.size() - 1;

        while (leftPointer < rightPointer)
        {
            while (!std::isalnum(s[leftPointer]) && leftPointer < rightPointer)
            {
                leftPointer++;
            }

            while (!std::isalnum(s[rightPointer]) && leftPointer < rightPointer)
            {
                rightPointer--;
            }

            if (std::tolower(s[leftPointer]) != std::tolower(s[rightPointer]))
            {
                return false;
            }
            leftPointer++;
            rightPointer--;
        }

        return true;
    }
};