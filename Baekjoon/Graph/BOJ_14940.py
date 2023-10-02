import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 시작 노드 위치 구하기
for idx_0, lst in enumerate(graph):
    if 2 in lst:
        start_row, start_col = idx_0, lst.index(2)


que = deque()


def BFS(graph, visited):
    # 시작 노드를 큐에 삽입.
    que.append([start_row, start_col])  # ex. start=[0,0]
    visited[start_row][start_col] = True
    graph[start_row][start_col] = 0  # 시작노드 값을 2에서 0으로 바꿈.

    while que:
        row_col = que.popleft()
        row, col = row_col[0], row_col[1]
        for dir_r, dir_c in direction:  # 동서남북으로 한칸씩 움직임
            new_r, new_c = row + dir_r, col + dir_c
            # cost = dist + 1
            if 0 <= new_r < n and 0 <= new_c < m:  # 움직인 위치가 지도 안인지 확인
                if graph[new_r][new_c] != 0 and visited[new_r][new_c] == False:  # 갈 수 있는 땅인지 확인
                    que.append([new_r, new_c])
                    graph[new_r][new_c] = graph[row][col] + 1
                    visited[new_r][new_c] = True


BFS(graph, visited)

# 원래 갈 수 있는 땅 중 목표지점에 도달할 수 없는 땅은 -1로 치환하기
for idx_r, lst_1d in enumerate(visited):
    for idx_c, x in enumerate(lst_1d):
        if x == False and graph[idx_r][idx_c] != 0:
            graph[idx_r][idx_c] = -1


for lst1 in graph:
    print(*lst1, sep=" ")