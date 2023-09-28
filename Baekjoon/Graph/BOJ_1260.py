from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#graph를 오름차순 정렬함.
graph = [sorted(lst) for lst in graph]
visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def dfs(v, visited):
    visited[v] = True
    print(v, end=' ')
    #현재 노드와 연결된 노드들을 재귀적으로 방문한다
    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited)


def bfs(start, visited):
    que = deque([start])
    visited[start] = True
    
    while que:
        v = que.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]: #방문하지 않은 노드면
                que.append(i)
                visited[i] = True
              
dfs(v, visited1)
print()
bfs(v, visited2)