x = int(input())
y = int(input())

time = 480 

x *= 2

for i in range(x):
    time += y

print(time// 60)
print(time% 60)
