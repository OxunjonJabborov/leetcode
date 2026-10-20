class Solution {
public:
    string defangIPaddr(string address) {
        string res = "";
        res.reserve(address.length() + 6);
        for (char c : address) {
            if (c == '.') {
                res += "[.]";
            } else {
                res += c;
            }
        }
        return res;
    }
};