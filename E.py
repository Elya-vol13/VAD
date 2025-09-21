x = int(input())
y = int(input())

if x > y:
    print (1)
else: 
    s = 0
    i = 1
    days = 0
    while s < y:
        s += i * (x + 2 * (i - 1))
        i += 1
        days += 1

    print(days)