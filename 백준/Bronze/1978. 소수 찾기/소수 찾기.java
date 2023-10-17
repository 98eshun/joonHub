

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));		
		int N = Integer.parseInt(br.readLine());
		int count = 0;
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		for(int i=0; i<N; i++) {
			int a = Integer.parseInt(st.nextToken());
			
			for(int j=2; j<=a; j++) {
				if(a==j) {
					count++;
					break;
				}
				if(a%j==0) {
					break;
				}
				
			}
		}
		System.out.println(count);
		
		
	}

}
