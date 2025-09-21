a = int(input())
b = int(input())
n = int(input())

op = b * n
while op >= a:
    n += op // a
    op = op % a + b * (op // a)

print(n)