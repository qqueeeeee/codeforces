n, m, a = map(int, input().split())

vert = (n + a - 1) // a
horiz = (m + a - 1) // a

sol = vert * horiz
print(sol)
