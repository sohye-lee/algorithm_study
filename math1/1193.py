num = int(input())

group = 1
while num > group:
    num -= group
    group += 1


if group % 2 == 0:
    print(f"{num}/{group - num + 1}")
else:
    print(f"{group-num + 1}/{num}")
