for _ in range(int(input())):
    ps_list = []
    try:
        for i in input():      
            if i == '(':
                ps_list.append(i)
            elif i == ')':
                ps_list.pop()
    except:
        print('NO')
        continue

    x = 'YES' if len(ps_list) == 0 else 'NO'
    print(x)