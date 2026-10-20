class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int max_w = 0;
        for (const auto& customer : accounts){
            int w = 0;
            for (int bank : customer) w += bank;
            if (w > max_w) max_w = w;
        }
        return max_w;
    }

};