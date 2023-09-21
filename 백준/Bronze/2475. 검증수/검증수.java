
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int[] list = new int[5];
		int result = 0;
		for(int i=0;i<5;i++) {
			list[i] = sc.nextInt();
		}
		for(int a : list) {
			result += a*a;
		}
		System.out.println(result%10);
	}

}
