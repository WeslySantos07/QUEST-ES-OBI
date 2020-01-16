t = [0]*3
d = [0]*3
d[0] = t[0] = int(input())
d[1] = t[1] = int(input())
d[2] = t[2] = int(input())

t.sort()

i = 0
j = 0

while j < 3: 
    if t[j] == d[i]:
        print(i+1)
        j = j + 1
        i = 0
    else:
         i = i + 1
