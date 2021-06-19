import sys

n = int(sys.stdin.readline(3))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)