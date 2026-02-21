class Solution {
public:
    int pivotInteger(int n) {
        int yigindi = n * (n + 1) / 2;
        int x = sqrt(yigindi);
        if(x * x == yigindi) return x;
        return -1;
    }
};
