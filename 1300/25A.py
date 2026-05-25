n = int(input())

odd: list[int] = []
even: list[int] = []

vals = map(int, input().split())

for i,val in enumerate(vals):
    if val % 2 == 0:
        even.append(i+ 1)
    else:
        odd.append(i+ 1)

if len(odd) >= 2:
    print(even[0])
else:
    print(odd[0])





