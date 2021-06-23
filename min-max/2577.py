a =int(input())
b =int(input())
c =int(input())

multi = a * b * c

loc = []
for i in range(10):
    loc.append(0)

for n in str(multi):
    loc[int(n)] += 1

for m in loc:
    print(m)


