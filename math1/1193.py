num = int(input())

ans = 0
n = 1
for i in range(0, num):
    for j in range(0,n):
        ans = str(j)+"/"+str(n-j)
    n += 1
print(ans)