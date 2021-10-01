x1=int(input())
x2=int(input())
n_max=1
n=1
k=1
while x1!=0 and x2!=0:
    while x1>=x2:
        n+=1
        k=1
        if x2==0:
            break
        if n>=n_max:
            n_max=n
            x1=x2
            x2=int(input())
        else:
            x1=x2
            x2=int(input())
    while x1<=x2:
        k+=1
        if x1==0:
            break
        if k>=n_max:
            n_max=k
            n=1
            x1=x2
            x2=int(input())
        else:
            x1=x2
            x2=int(input())
    while x1==x2:
        n=k=1
        x1=x2
        x2=int(input())
print(n_max)
