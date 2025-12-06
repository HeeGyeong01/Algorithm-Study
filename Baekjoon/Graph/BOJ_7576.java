import java.io.*;
import java.util.*;

public class BOJ_7576 {
  static int greenTomato, day;
  static int m, n;
  static int[][] grid;
  static Deque<Loc> que;
  static int[] dr = { 1, 0, -1, 0 };
  static int[] dc = { 0, -1, 0, 1 };

  static class Loc {
    int row, col;

    public Loc(int row, int col) {
      this.row = row;
      this.col = col;
    }
  }

  public static void main(String[] args) throws IOException {
    greenTomato = 0;
    day = 0;
    que = new ArrayDeque<>();
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st;
    st = new StringTokenizer(br.readLine());
    m = Integer.parseInt(st.nextToken());
    n = Integer.parseInt(st.nextToken());

    // 0. 격자판 입력 받음
    grid = new int[n][m];
    for (int row = 0; row < n; row++) {
      st = new StringTokenizer(br.readLine());
      for (int col = 0; col < m; col++) {
        grid[row][col] = Integer.parseInt(st.nextToken());
        // 익지 않은 토마토인 경우 그 수를 변수에 저장해 놓음.
        if (grid[row][col] == 0) {
          greenTomato += 1;
          // 익은 토마토인 경우 큐에 넣음.
        } else if (grid[row][col] == 1) {
          que.add(new Loc(row, col));
        }
      }
    }

    // 1. 모든 토마토가 익어있는 경우
    if (greenTomato == 0) {
      System.out.println(0);
      return;
    }

    // 2. 전체 격자 훑으면서 BFS 실행
    while (greenTomato > 0) {
      day += 1;
      int greenToRedCount = 0;
      int countPerDay = que.size();

      // 직전에 익은 토마토 순회
      for (int count = 0; count < countPerDay; count++) {
        Loc nextLoc = que.poll();
        int curRow = nextLoc.row;
        int curCol = nextLoc.col;

        // 사방 탐색
        for (int dir = 0; dir < 4; dir++) {
          int nextRow = curRow + dr[dir];
          int nextCol = curCol + dc[dir];
          boolean inBounds = nextRow < n && nextRow >= 0 && nextCol < m && nextCol >= 0;

          // 격자판 범위 안이고 안 익은 토마토면
          if (inBounds && grid[nextRow][nextCol] == 0) {
            greenToRedCount += 1;
            greenTomato -= 1;
            grid[nextRow][nextCol] = 1;
            que.add(new Loc(nextRow, nextCol));
          }
        }
      }

      // 3. 토마토를 익히지 못하는 날인 경우
      if (greenToRedCount == 0) {
        System.out.println(-1);
        return;
      }
    }

    // 4. 다 익은 토마토로 채운 경우
    System.out.println(day);

  }
}