import math

x = int(input())
y = int(input())
n = int(input())

if x > n:
    print(1)
else:
    if x > n:
        print(1)
    else:      
        if (n - x) % (x - y) == 0:
          days =  2 + (math.ceil((n - x) / (x - y)))      
        
        else:
            days = 1 + (math.ceil((n - x) / (x - y))) 

        print(days)
        