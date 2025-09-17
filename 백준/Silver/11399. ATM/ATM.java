import java.io.IOException;
import java.util.*;

/* baekjoon_11399 ATM : 그리드 알고리즘 */
public class Main {

    static int result = 0;

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        // 인출하는 사람 수
        int pernum = sc.nextInt();
        List<Integer> times = new ArrayList<>();

        for (int i = 0; i < pernum; i++) {
            times.add(sc.nextInt());
        }

        times.sort(Comparator.naturalOrder());

        int total = 0;
        int sum = 0;

        for (int time : times) {
            sum += time;     // 개별 사람의 대기 시간
            total += sum;    // 전체 합에 추가
        }

        System.out.println(total);
    } // main
}
