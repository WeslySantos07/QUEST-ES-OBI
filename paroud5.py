n = [int(input()), int(input()), int(input())]
c = 0
    
for i in range(3):
    if n[i] % 2 == 0:
        c += 1
    elif n[i] % 5 == 0:
         c += 1
                      
print(c)
