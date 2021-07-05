word = input().upper()
alphabets = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
ans = 0
for letter in word:
    for a in alphabets:
        if letter in a:
            ans += alphabets.index(a) + 3

print(ans)