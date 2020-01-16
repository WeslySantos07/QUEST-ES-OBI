n = list(map(int, input().split()))
n.sort()

if n[0] == n[1] and n[1] == n[2]:
    print("a")
elif n[2] >= (n[0]+n[1]):
    print("n")
elif n[2]**2 == ((n[0]**2)+(n[1]**2)):
    print("r")
else:
    print("o")
