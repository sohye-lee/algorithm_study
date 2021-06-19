import sys

n = int(sys.stdin.readline())
for i in range(1, n+1):
    nums = sys.stdin.readline(4).split(" ")
    a = int(nums[0])
    b = int(nums[1])
    print(f"Case #{i}: {a+b}")