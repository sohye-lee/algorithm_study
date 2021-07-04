word = input().lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
li = []
for a in alphabet:
    if a not in word:
        li.append(str(-1))
    else:
        li.append(str(word.index(a)))
print(" ".join(li))