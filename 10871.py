import sys

nums = sys.stdin.readline().split(" ")
n = int(nums[0])
x = int(nums[1])
li = sys.stdin.readline().split(" ")
result = []
for i in li[:n]:
    i = int(i)
    if i < x:
        result.append(str(i))
print(" ".join(result))
