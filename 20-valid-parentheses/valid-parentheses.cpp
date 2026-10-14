class Solution {
public:
    bool isValid(string s) {
        
        // First, create a stack to track characters
        std::stack<char> currentStack;

        // Iterate though the string s
        for (char c : s)
        {
            if (c == '[' or c == '{' or c == '(')
            {
                currentStack.push(c);
            }

            else if (c == ']' || c == '}' || c == ')')
            {
                if (currentStack.empty() == true)
                {
                    return false;
                }

                char topChar = currentStack.top();

                if ((c == ']' && topChar == '[') || 
                    (c == '}' && topChar == '{') || 
                    (c == ')' && topChar == '('))
                {
                    currentStack.pop();
                }
                else
                {
                    return false;
                }
            }
        }

        if (currentStack.empty() != true)
        {
            return false;
        }

        return true;

    }
};