import sys

times = int(sys.stdin.readline(8))
for i in range(times):
    nums = sys.stdin.readline(10).split(" ")
    a = int(nums[0])
    b = int(nums[1])
    print(a + b)
