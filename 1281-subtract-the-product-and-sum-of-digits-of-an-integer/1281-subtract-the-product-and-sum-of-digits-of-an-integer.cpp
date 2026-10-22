class Solution {
public:
    int subtractProductAndSum(int n) {
        string s = to_string(n);
        int kop = 1, yig = 0;
        while(n > 0){
            kop *= n % 10;
            yig += n % 10;
            n /= 10;
        }
        return kop - yig;
    }
};