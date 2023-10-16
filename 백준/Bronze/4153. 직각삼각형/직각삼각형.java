

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		while(true){
			
			String s = br.readLine();
			StringTokenizer st = new StringTokenizer(s, " ");
			int[] a = new int[3];
			
			
			for(int i=0;i<3;i++) {
				a[i] = Integer.parseInt(st.nextToken());
			}
			
			Arrays.sort(a);
			int b = (a[0] * a[0]) + (a[1] * a[1]);
			int c = a[2] * a[2];
			
			if(a[0]==0 && a[1]==0 && a[2]==0) {
				break;
			}
			
			if(c == b) {
				System.out.printf("right\n");
			}else {
				System.out.printf("wrong\n");
			}
			
		
		}
		
		
	
	}

}
