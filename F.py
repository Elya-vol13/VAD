n = int(input())
s = int(input())

if s < 1 or s > 9 * n:
    print("NO")
else:
    num = ['0'] * n
    num[0] = '1'
    s -= 1
    
    for i in range(n-1, 0, -1):
        add = min(9, s)
        num[i] = str(int(num[i]) + add)
        s -= add
    
    if s > 0:
        num[0] = str(int(num[0]) + s)
    
    print(''.join(num))