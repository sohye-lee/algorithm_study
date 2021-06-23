nums = []
for i in range(10):
    nums.append(int(input()))

def leftover(num):
    return num%42

nums = map(leftover, nums)
print(len(set(nums)))
