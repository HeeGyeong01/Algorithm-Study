m, n = map(int, input().split())

isPrime = [True] * (n + 1)
isPrime[0], isPrime[1] = False, False

# n 이하의 소수를 에라토스테네스의 체를 이용하여 구해 놓음
for x in range(2, n + 1):
    for y in range(x, n + 1):
        if x * y > n:
            break
        isPrime[x * y] = False

print(*[i for i, x in enumerate(isPrime) if x == True and i >= m], sep="\n")