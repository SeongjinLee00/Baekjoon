import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(br.readLine());

        int now = 3600*h + 60*m + s;
        now += t;
        
        h = now/3600;
        now -= h*3600;
        h = h%24;
        m = now/60;
        now -= m*60;

        System.out.println(h + " " + m + " " + now);
    }
}