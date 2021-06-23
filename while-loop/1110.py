num = int(input(""))
n = num
cycle = 0

while True:
    a = n//10
    b = n%10
    c = a + b

    n = b*10 + c%10
    cycle = cycle + 1
    if n == num:
        break

print(cycle)


