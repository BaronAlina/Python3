pr = int(input())
a = 0
while pr != 0:
    n = int(input())
    if n != 0 and pr < n:
        a += 1
    pr = n
print(a)
