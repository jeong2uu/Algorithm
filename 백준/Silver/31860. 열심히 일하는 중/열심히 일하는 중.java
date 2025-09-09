import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < N; i++) {
            pq.add(Integer.parseInt(br.readLine().trim()));
        }

        br.close();

        int satisfactionPrev = 0;
        int dayCount = 0;
        StringBuilder result = new StringBuilder();

        while (!pq.isEmpty()) {
            dayCount++;
            int currentImportance = pq.poll();
            int satisfactionToday = (satisfactionPrev / 2) + currentImportance;
            result.append(satisfactionToday).append("\n");
            satisfactionPrev = satisfactionToday;

            currentImportance -= M;
            if (currentImportance > K) {
                pq.add(currentImportance);
            }
        }

        System.out.println(dayCount);
        System.out.print(result);
    }
}