ct = int(input())
for i in range(ct):
    scores = input()
    result = 0
    o = 0
    for s in scores:
        if s == 'O':
            o += 1
            result += o
        else:
            o = 0
    print(result)

