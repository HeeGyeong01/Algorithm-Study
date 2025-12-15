import java.util.*;
import java.io.*;

public class BOJ_1932 {

  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int n = Integer.parseInt(br.readLine());

    int maxSum = 0;
    int[] dp = new int[n];
    int[] curLine = new int[n];

    for (int count = 1; count <= n; count++) {
      StringTokenizer st = new StringTokenizer(br.readLine());
      // 현재 줄을 curLine에 입력받음.
      for (int idx = 0; idx < count; idx++) {
        curLine[idx] = Integer.parseInt(st.nextToken());
      }

      for (int idx = count - 1; idx >= 0; idx--) {

        // 오른쪽 대각선 위
        dp[idx] = curLine[idx] + dp[idx];

        // 왼쪽 대각선 위(존재하는지 확인한 후)
        if (idx - 1 >= 0) {
          dp[idx] = Math.max(dp[idx], curLine[idx] + dp[idx - 1]);
        }
      }

    }

    for (int item : dp) {
      maxSum = Math.max(maxSum, item);
    }

    System.out.println(maxSum);
    return;
  }

}
