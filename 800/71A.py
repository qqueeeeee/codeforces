n = int(input())
fin = ""

for i in range(0,n):
    word = input()
    if len(word) > 10:
        fin += f"{word[0]}{len(word) - 2}{word[-1]}\n"
    else:
        fin += f"{word}\n"
print(fin)

