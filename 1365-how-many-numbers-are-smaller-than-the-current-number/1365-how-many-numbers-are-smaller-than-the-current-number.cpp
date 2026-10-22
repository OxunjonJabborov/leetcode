class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        vector<int> count(101, 0);
        for (int x : nums)
            count[x]++;
        for (int i = 1; i <= 100; ++i)
            count[i] += count[i - 1];
        vector<int> ans;
        ans.reserve(nums.size());
        for (int x : nums)
            ans.push_back(x == 0 ? 0 : count[x - 1]);
        return ans;
    }
};
