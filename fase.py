n,k = int(input()),int(input())

v = [0]*n

for i in range(n):
    v[i] = int(input())

v.sort()
v.reverse()

i = 1
r  = 0

for c in range(n-1):
    
    if i == k:
        if v[c] == v[c+1]:
            k += 1
        else:
            break 
    i += 1

print(i)
