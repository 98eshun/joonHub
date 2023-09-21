
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int x = sc.nextInt();
		
		int[] array = new int[n];
		
		for(int a=0;a<array.length;a++) {
			array[a] = sc.nextInt();
		}
		for(int k : array) {
			if(x>k) {
				System.out.printf("%d ",k);
			}
		}
	}

}
