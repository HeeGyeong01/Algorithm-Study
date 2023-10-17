import sys
from collections import deque

input = sys.stdin.readline
direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]   
visited = [[False] * m for _ in range(n)]

#시작 노드 위치 구하기
for idx, lst in enumerate(graph):
    if 2 in lst:
        start_row, start_col = idx, lst.index(2)
        
   

def BFS(start_r, start_c):
    #시작 노드를 큐에 삽입
    que = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    graph[start_r][start_c] = 0  #시작 노드의 값을 2에서 0으로 변경함
    
    while que: #큐 안에 원소가 남아있으면
        row, col = que.popleft()
        for dr, dc in direction:  #동서남북으로 한칸씩 움직임
            nr, nc = row+dr, col+dc
            if 0<=nr<n and 0<=nc<m:  #움직인 위치가 지도 안인지 확인
                #갈 수 없는 땅인 값이 0인 노드와 이미 방문한 노드는로는 이동하지 않는다.
                if graph[nr][nc] != 0 and visited[nr][nc] == False: 
                    graph[nr][nc] = graph[row][col] +1
                    que.append((nr, nc))
                    visited[nr][nc] =True
                    
            

BFS(start_row, start_col)

# 원래 갈 수 있는 땅 중 목표지점에 도달할 수 없는 땅은 -1로 치환하기
for idx_r, lst_1d in enumerate(visited):
    for idx_c, x in enumerate(lst_1d):
        if x == False and graph[idx_r][idx_c] != 0:
            graph[idx_r][idx_c] = -1

for lst1 in graph:
    print(*lst1, sep=" ")