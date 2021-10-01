a1=int(input())
a=int(input())
if a==0:
    a3=0
else:
    a3=int(input())
s=0
while a3!=0:
    if a1<a and a3<a:
        s+=1
    a1=a
    a=a3
    a3=int(input())
print(s)
