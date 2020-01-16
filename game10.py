n = int(input())
d = int(input())
a = int(input())

cont = 0


if a > d:
    cont = n - (a-d)
else:
    cont = d - a

print(cont)
