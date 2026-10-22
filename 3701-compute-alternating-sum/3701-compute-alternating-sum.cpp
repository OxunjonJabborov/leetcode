class Solution {
public:
    int alternatingSum(vector<int>& nums) {
       int juft = 0, toq = 0;
       for(int i = 0; i < nums.size(); i += 2)
       juft += nums[i];
       for(int i = 1; i < nums.size(); i += 2)
       toq += nums[i];
       return juft - toq;
    }
};