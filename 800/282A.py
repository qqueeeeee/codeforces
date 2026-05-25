n = int(input())
x = 0

for i in range(0,n):
    op = input()
    if "+" in op:
        x += 1
    else:
        x -= 1
print(x)
