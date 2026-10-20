class Solution {
public:
    vector<int> transformArray(vector<int>& nums) {
        int odds = count_if(nums.begin(), nums.end(), [](int i){ return i % 2 != 0;});
        int evens = nums.size() - odds;
        vector<int> ans(evens, 0);
        ans.insert(ans.end(), odds, 1);
        return ans;
    }
};