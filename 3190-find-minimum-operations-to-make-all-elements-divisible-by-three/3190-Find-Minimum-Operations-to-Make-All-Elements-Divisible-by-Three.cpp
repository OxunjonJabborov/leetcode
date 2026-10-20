class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int counter = 0;
        for (int i : nums){
            if (i % 3 == 1 || i % 3 == 2) counter++;
        }
        return counter;
    }
};