b = int(input())
q = 0
for i in range(b):
    var = list(map(int, input().split()))
    if var[0] > var[1]:
        q += var[1]
print(q)
