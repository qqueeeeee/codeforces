s = input()

VOWELS = ['a','e','i','o','u', 'y']
res = ''

for i in s:
    if i.lower() in VOWELS:
        continue
    else:
        res += f".{i.lower()}"

print(res)



    
