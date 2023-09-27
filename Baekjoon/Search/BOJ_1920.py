import sys

input()
a = sorted(list(map(int, sys.stdin.readline().split())))
input()
b = list(map(int, sys.stdin.readline().split()))


def in_a(x):
    start, end = 0, len(a) - 1

    while start <= end:
        mid = (start + end) // 2
        if a[mid] == x:
            return True
        elif a[mid] > x:
            end = mid - 1
        elif a[mid] < x:
            start = mid + 1
    return False


for i in b:
    if in_a(i):
        print(1)
    else:
        print(0)