n = [0]*10
for i in range(10):
    n[i] = int(input())
n.sort()
i = 0
ct = 1
while ct <= 20:
    print(n[i], end=' ')
    if ct == 10:
        n.reverse()
        i = -1
        print("\n")
    i+=1
    ct+=1
