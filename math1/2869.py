import math

A, B, V = list(map(int, input().split()))
ans = (V - B) / (A - B)
print(math.ceil(ans))