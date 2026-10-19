class Solution {
public:
    int differenceOfSums(int n, int m) {
      int javob = 0;
      int bolinadi = 0;
      int bolinmaydi = 0;
      for(int i = 1; i <= n; i++){
        if (i % m == 0)
          bolinadi += i; 
        else 
          bolinmaydi += i;
      }
      javob = bolinmaydi - bolinadi;
      return javob;
    }
};