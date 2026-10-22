class Solution {
public:
    bool isValid(string s) {
        stack<char> st;

        for (char c : s) {
            if (c == '(' || c == '[' || c == '{') {
                st.push(c); // push
            } else {
                if (st.empty()) return false; // agar st bo‘sh bo‘lsa return false
                else if ((c == ')' && st.top() != '(') || 
                (c == ']' && st.top() != '[') ||
                (c == '}' && st.top() != '{'))
                    return false; // agar top mos bo‘lmasa return false
            
                else st.pop(); // aks holda pop
            }
        }
        return st.empty(); // oxirida st bo‘sh bo‘lsa true, bo‘lmasa false
    }
};