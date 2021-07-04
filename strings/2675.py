case = int(input())
for i in range(0,case):
    s = input().split()
    ans = ""
    r = int(s[0])
    p = s[1]
    for letter in p:
        ans += letter*r
    print(ans)
    
        