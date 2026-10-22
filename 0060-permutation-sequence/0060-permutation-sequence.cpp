class Solution {
public:
    string getPermutation(int n, int k) {
        vector<int> raqamlar;
        vector<int> factorial(n + 1, 1);
        for (int i = 1; i <= n; i++) {
            raqamlar.push_back(i);
            factorial[i] = factorial[i-1] * i;
        }
        k--;
        string natija = "";
        for (int i = n; i >= 1; i--) {
            int idx = k / factorial[i - 1];
            natija += to_string(raqamlar[idx]);
            raqamlar.erase(raqamlar.begin() + idx);
            k %= factorial[i - 1];
        }
        return natija;
    }
};