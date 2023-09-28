# Dynamic Programming -> 메모리 공간을 더 쓰는 대신 수행시간을 줄이는 기법
n = int(input())
d = [0] * (n+1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)

print(d[n])