import sys

is_on = True
while is_on:
    nums = sys.stdin.readline(6)
    nums = nums.split(" ")
    a = int(nums[0])
    b = int(nums[1])
    if [a,b] == [0,0]:
        is_on = False
    else:
        print(a+b)