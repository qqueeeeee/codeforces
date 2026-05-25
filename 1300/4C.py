hash: dict[str, int]  = {} 

n = int(input())

for i in range(n):
    user = input()
    if user not in hash:
        hash[user] = 1
        print("OK")
    else:
        print(f"{user}{hash[user]}")
        hash[user] += 1

