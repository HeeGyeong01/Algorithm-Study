#유니온 파인드
#크루스칼 알고리즘

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]  # 루트 노드 찾은 경우


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:  # b가 더 작거나 a=b일 때
        parent[a] = b


# 노드와 간선 수 입력받음
v, e = map(int, input().split())
parent = [0] * (v + 1)

edges = []
result = 0  # 최소 비용 담을 변수
max_cost = 0  # 간선의 최대 가중치

# 부모테이블 초기화
for i in range(1, v + 1):
    parent[i] = i

# 간선 정보 입력받음
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()  # 튜플의 첫번째 원소인 cost값을 기준으로 오름차순 정렬

for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함시킴
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
        if cost > max_cost:
            max_cost = cost


print(result - max_cost)