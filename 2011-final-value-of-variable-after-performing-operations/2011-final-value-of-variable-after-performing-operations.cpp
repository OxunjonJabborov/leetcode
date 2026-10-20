class Solution {
public:
    int finalValueAfterOperations(vector<string>& operations) {
        return accumulate(operations.begin(), operations.end(), 0, [](int sum, const string& op) {
            return sum + (op[1] == '+' ? 1 : -1);
        });
    }
};