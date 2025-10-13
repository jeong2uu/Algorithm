import java.io.IOException;
import java.util.*;

/* baekjoon_6603 로또 : 백트래킹 | 재귀 */
public class Main {

    static int k;
    static int[] s;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            k = sc.nextInt();
            if (k == 0) break;

            s = new int[k];
            visited = new boolean[k];

            for (int i = 0; i < k; i++) {
                s[i] = sc.nextInt();
            }

            dfs(0, 0);
            sb.append("\n");
        }
        System.out.print(sb.toString());
    }

    static void dfs(int start, int depth) {
        if (depth == 6) {
            for (int i = 0; i < k; i++) {
                if (visited[i]) sb.append(s[i]).append(" ");
            }
            sb.append("\n");
            return;
        }

        for (int i = start; i < k; i++) {
            visited[i] = true;
            dfs(i + 1, depth + 1);
            visited[i] = false;
        }
    }
}
