a=-1
p=0
c=0
mx=1
while a!=0:
    a=int(input())
    if(a!=p):
        if c>=mx:
            mx=c
        c=0
    p=a
    c=c+1
print(mx)
