a = int(input())
f = [int(input()), int(input()), 0]
f[2] = a - sum(f)
print(max(f))