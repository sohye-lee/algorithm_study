word = input().upper()

unique_letters = list(set(word))
ct = []

for l in unique_letters:
    ct.append(word.count(l))
if ct.count(max(ct)) >= 2:
    print("?")
else:
    print(unique_letters[ct.index(max(ct))])
        

