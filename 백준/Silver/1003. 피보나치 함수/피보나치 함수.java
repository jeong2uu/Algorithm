import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();   // 테스트 케이스 개수

        // 미리 최대 n까지 0, 1 호출 횟수 저장
        int[][] dp = new int[41][2]; // n은 최대 40까지만 입력됨 (문제 조건)

        // 초기값
        dp[0][0] = 1; // fibonacci(0) 호출 시 -> 0이 1번 출력
        dp[0][1] = 0;

        dp[1][0] = 0; // fibonacci(1) 호출 시 -> 1이 1번 출력
        dp[1][1] = 1;

        // 점화식으로 채우기
        for (int i = 2; i <= 40; i++) {
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]; // 0의 개수
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]; // 1의 개수
        }

        // 입력받아서 출력
        for (int t = 0; t < T; t++) {
            int n = sc.nextInt();
            System.out.println(dp[n][0] + " " + dp[n][1]);
        }

        sc.close();
    } // main
}