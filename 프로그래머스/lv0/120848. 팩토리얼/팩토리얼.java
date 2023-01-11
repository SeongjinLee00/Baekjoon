class Solution {
    public int factorial(int n) {
        if (n==1 || n==0){
            return 1;
        }
        return n*factorial(n-1);
    }
    public int solution(int n) {
        int answer = 1;
        
        for (int i=1;i<11;i++){
            if (factorial(i)>n){
                return i-1;
            }
        }
        
        return 10;
    }
}