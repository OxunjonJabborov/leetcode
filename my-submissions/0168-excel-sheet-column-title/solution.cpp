class Solution {
public:
    string convertToTitle(int columnNumber) {
        string natija;
        while (columnNumber > 0){
            columnNumber--;
            natija = char(columnNumber % 26 + 'A') + natija;
            columnNumber /= 26;
        }
        return natija;
    }
};
