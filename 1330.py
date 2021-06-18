nums = input("")

def compare(nums):
    [a,b] = nums.split(" ")
    a = int(a)
    b = int(b)
    if a > b:
        print(">")
    elif a == b:
        print("==")
    else:
        print("<")

compare(nums)