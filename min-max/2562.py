nums = []
for i in range(9):
    nums.append(int(input()))

max = 0
loc = 0
count = 0

for n in nums:
    count += 1
    if n > max:
        max = n
        loc = count
    
print(max)
print(loc)
