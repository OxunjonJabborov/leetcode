class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int counter = 0;
        return count_if(nums.begin(), nums.end(), [](int x){
            return x % 3 != 0;
        });
    }
};