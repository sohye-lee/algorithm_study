ct = int(input())

for i in range(0,ct):
    h, w, n = list(map(int, input().split()))
    check_story = n%h == 0
    if check_story:
        print(h*100 + n//h)
    else:
        print(n%h*100 + n//h+1)
    
