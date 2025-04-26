class Solution {
public:
    int numberOfEmployeesWhoMetTarget(vector<int>& hours, int target) {
        int k = 0;
        for(int x: hours){
            if(x >= target) k += 1;
        }
        return k;
    }
};
