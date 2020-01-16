pc = list(map(int, input().split()))

n1 = pc[0]*pc[1]
n2 = pc[2]*pc[3]

if n1 == n2:
    print(0)
elif n1 > n2:
    print(-1)
else:
    print(1)
