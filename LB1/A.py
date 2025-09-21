n = int(input())

s = 0
for i in range(1, n+1):
    s += (2 * i) / (i + 2) 

print(round(s, 3))
