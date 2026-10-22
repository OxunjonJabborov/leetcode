class Solution {
public:
    int findClosest(int x, int y, int z) {
        int farq1, farq2;
        farq1 = abs(z - x);
        farq2 = abs(y - z);
        if(farq1 < farq2)
        return 1;
        else if(farq1 > farq2)
        return 2;
        else return 0;
    }
};