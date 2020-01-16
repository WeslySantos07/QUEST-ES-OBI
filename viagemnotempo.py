a,b,c = list(map(int, input().split()))

if a==b or a==c or b==a or b==c:
    print("S")
elif a+b==c or a+c==b or b+c==a:
    print("S")
else:
    print("N");
