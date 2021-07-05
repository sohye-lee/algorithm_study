word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ct = 0

for l in croatia:
    if l in word:
        ct += word.count(l)
        word = word.replace(l, ' ')

word = word.replace(' ', '')

print(ct+len(word))

