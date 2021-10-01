import java.util.*;

public class Main {
// 특정한시각안에'3'이포함되어있는지의여부
	public static boolean check(int h, int m, int s) {
		if(h % 10== 3|| m / 10== 3|| m % 10== 3|| s / 10== 3|| s % 10== 3)
			return true;
		return false;
	}
	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in);
		// H를입력받기
		int h = sc.nextInt();
		int cnt= 0;
		for(int i= 0; i<= h; i++) {
			for(int j = 0; j < 60; j++) {
				for(int k = 0; k < 60; k++) {
					// 매시각안에'3'이포함되어있다면카운트증가
					if(check(i, j, k)) cnt++;
				}
			}
		}
		System.out.println(cnt);
	}
}
