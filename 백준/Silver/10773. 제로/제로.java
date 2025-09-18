import java.io.IOException;
import java.util.*;

/* baekjoon_10773 제로 : 구현|자료구조|스택 */
public class Main {

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        // 정수입력
        int testcase = sc.nextInt();
        ArrayList<Integer> money = new ArrayList<>();

        // 정수를 testcase만큼 입력 0 < x < 1000000 사이
        for (int i = 0; i < testcase; i++) {
            int num = sc.nextInt();
            if (num == 0 && !money.isEmpty()) {
                money.remove(money.size() - 1); // 마지막 값 제거
            } else {
                money.add(num);
            }
        }

        int result = money.stream().mapToInt(Integer::intValue).sum();
        System.out.println(result);


    } // main
}
