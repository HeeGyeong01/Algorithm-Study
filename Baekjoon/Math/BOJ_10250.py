# 실수했던 거: 최상층에 배정하는 케이스를 고려 안 함

for _ in range(int(input())):
    h, w, n = map(int, input().split())
    
    YY = h if n%h == 0 else n%h

    XX = (n//h) if n%h == 0 else (n//h)+1
    XX = '0'+str(XX) if XX < 10 else XX
    
    print(YY, XX, sep='')