class Solution {
public:
    bool oziga_ozi_bolinadimi(int n) {
        for (char i : to_string(n)) {
            if (i == '0' || n % (i - '0') != 0)
                return false;
        }
        return true;
    }

    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> natija;
        for (int n = left; n <= right; n++)
            if (oziga_ozi_bolinadimi(n))
                natija.push_back(n);
        return natija;
    }
};