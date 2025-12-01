import java.util.*;

class Solution {
    public int solution(String[] friends, String[] gifts) {
        int peopleSum = friends.length;

        // 0. 사람의 이름을 0 ~ n-1 정수로 매핑함.
        Map<String, Integer> nameToNum = new HashMap<>();
        for (int num = 0; num < peopleSum; num++) {
            nameToNum.put(friends[num], num);
        }
        // 1. 사람 수X사람수 크기의 2차원 배열 생성
        int[][] giftInfo = new int[peopleSum][peopleSum];

        // 2. 선물 기록을 바탕으로 누구랑 주고받았는지, 해당 사람의 선물 지수를 저장
        for (String gift : gifts) {
            int from = nameToNum.get(gift.split(" ")[0]);
            int to = nameToNum.get(gift.split(" ")[1]);

            giftInfo[from][to] += 1; // 선물 준 정보 저장
            giftInfo[from][from] += 1; // 보내는 사람의 선물지수 +1
            giftInfo[to][to] -= 1; // 받는 사람의 선물지수 -1
        }

        // 3. 각 사람이 다음 달에 받는 선물의 개수를 저장하는 1차원 배열 생성
        int[] giftSum = new int[peopleSum];

        // 4. 다음달에 받는 선물 수 계산
        for (int a = 0; a < peopleSum; a++) {
            for (int b = a + 1; b < peopleSum; b++) {

                // 4-1. 둘이 주고받은 수가 같거나 주고받은 기록이 없다면
                if ((giftInfo[a][b] == giftInfo[b][a]) || (giftInfo[a][b] == 0 && giftInfo[b][a] == 0)) {
                    // 선물 지수가 더 큰 사람이 선물 하나를 받음.
                    if (giftInfo[a][a] > giftInfo[b][b])
                        giftSum[a] += 1;
                    if (giftInfo[a][a] < giftInfo[b][b])
                        giftSum[b] += 1;

                }

                // 4-2. 선물을 주고받은 기록이 있다면 더 많이 준 사람이 받음.
                if (giftInfo[a][b] > giftInfo[b][a]) {
                    giftSum[a] += 1;
                } else if (giftInfo[a][b] < giftInfo[b][a]) {
                    giftSum[b] += 1;
                }

            }
        }

        int maxAmount = Integer.MIN_VALUE;
        for (int amount : giftSum) {
            maxAmount = Math.max(maxAmount, amount);
        }

        return maxAmount;
    }
}