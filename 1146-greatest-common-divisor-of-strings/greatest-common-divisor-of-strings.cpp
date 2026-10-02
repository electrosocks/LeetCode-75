class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        
        // First, let's check if they are same in either direction
        if (str1 + str2 != str2 + str1)
        {
            return "";
        }

        // Now, let's find the smallest common denominator
        int gdcLength = gcd(str1.size(), str2.size());
        return str1.substr(0, gdcLength);

    }
};