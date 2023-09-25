n = int(input())
nums = set(map(int, input().split()))

# 1000 이하의 소수를 에라토스테네스의 체 를 이용하여 구해 놓음.
prime_nums = [i for i in range(2, 1001)]

for i in prime_nums:
    for x in prime_nums:
        if x >i and x % i == 0:
            prime_nums.remove(x)

prime_nums = set(prime_nums)
print(len(nums&prime_nums))