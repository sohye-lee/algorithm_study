nums = input().split()
reverses = []
for n in nums:
    a = ""
    for l in n:
        a = l + a
    reverses.append(int(a))

print(max(reverses))
    