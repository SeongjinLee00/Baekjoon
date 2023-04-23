class Solution {
    public int solution(int[] num_list) {
        int s = 0;
        int p = 1;
        for (int num : num_list){
            s += num;
            p *= num;
        }
        
        if (p>s*s) return 0;
        return 1;
    }
}