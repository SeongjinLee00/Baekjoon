import java.util.*;

class Solution {
    public ArrayList solution(int n, int k) {
        ArrayList answer = new ArrayList();
        for (int i=1; i<=n; i++){
            if(i%k==0) {
                answer.add(i);
            }
        }
        return answer;
    }
}