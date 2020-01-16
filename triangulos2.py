n = list(map(int, input().split()))
n.sort()

if n[2] >= n[1] + n[0]:
    print('n')
elif n[2]*n[2] < n[1]*n[1] + n[0]*n[0]:
    print('a')
elif n[2]*n[2] > n[1]*n[1] + n[0]*n[0]:
    print('o')
else:
    print('r')
