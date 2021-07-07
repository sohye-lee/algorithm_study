num = int(input())
import math

# 6 -> 12 -> 18 -> 24
ans = 1
room = 1
while room + 6 * ans < num:
    room +=  6 * ans
    ans += 1
    print(room)
if num == 1:
    print(1)
else:
    print(ans + 1)