n = int(input())
asdf = list(map(int, input().split(" ")))

asdf[0] = asdf[0] - (asdf[3] + asdf[4])
asdf[1] = asdf[1] - (asdf[3] + asdf[5])
asdf[2] = asdf[2] - (asdf[4] + asdf[5])
res = 0

for i in range(7):
    res += asdf[i]

if res == n:
    print("N")
else:
    print("S")
