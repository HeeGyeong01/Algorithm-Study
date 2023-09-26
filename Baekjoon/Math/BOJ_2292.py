n = int(input())
coef, bounded_num = 1, 1

for i in range(2, n+1):
    if i <= bounded_num:
        continue
    bounded_num += coef*6
    coef += 1

print(coef)


# 다른 풀이
# 위의 풀이에 비해서 시간이 10배 단축됨
n = int(input())
coef, bound = 1, 1

while n > bound:
    bound += coef*6
    coef +=1

print(coef)