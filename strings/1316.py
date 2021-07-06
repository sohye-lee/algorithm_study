ct = int(input())

def compress(word):
    word = list(word.upper())
    ans = list()
    for i in range(0, len(word)):
        if i == 0:
            ans.append(word[i])
        elif word[i] != word[i-1]:
            ans.append(word[i])
    return ans

def word_check(letters):
    abc = list(range(65,91))
    abc = list(map(chr, abc))
    for letter in letters:
        if letter not in abc:
            return False
        else:
            abc.remove(letter)
    return True

ans = 0
for i in range(0, ct):
    word = input()
    compressed = compress(word)
    checked = word_check(compressed)
    if checked:
        ans += 1

print(ans)
