n = int(input())
ct = 0

if n <= 99:
    ct = n
else:
    ct = 99
    for i in range(100, n+1):
        digit_nums = list(map(int, str(i)))
        if digit_nums[0] - digit_nums[1] == digit_nums[1] - digit_nums[2]:
            ct += 1
        
print(ct)
