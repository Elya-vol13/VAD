x = int(input())

while True:
    if len(str(x)) == len(set(str(x))):
        break
    x -= 1
print (x)
