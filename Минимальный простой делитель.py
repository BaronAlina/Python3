n=int(input())
if n%2 == 0:
    print (2)
else:
    i = 3
    while n%i != 0 and i*i <= n:
        i+= 2
    if i*i <= n:
        print(i)
    else:
        print(n)
