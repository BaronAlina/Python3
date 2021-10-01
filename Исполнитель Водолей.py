lim = 10**5
A = int(input())
B = int(input())
n = int(input())
min = 'A'
max = 'B'
a = 0
b = 0
real = False
 
if A>=B:
  c = B
  B = A
  A = c
  z = min
  min = max
  max = z
 
k=0
while k<=lim:
  if a == 0 and (a!=n and b!=n):
      a = A
      k += 1
      continue
  elif (b == 0 or (B-b)>=a) and (a!=n and b!=n):
      b = b+a
      a = 0
      k += 1
      continue
  elif (B-b)<=a and (a!=n and b!=n):
      b = B
      a = a-(B-b)
      k += 1
      continue
  elif b==B and (a!=n and b!=n):
      b = 0
      k += 1
      continue
  elif a!=A and b!=B and b-(A-a)==n and (a!=n and b!=n):
      b = b - (A-a)
      a = A
      k += 1
      continue
  else:
      real = True
      break
 
if real == True:
  while True:
    if a == 0 and (a!=n and b!=n):
      a = A
      print('>', min)
      continue
    if (b == 0 or (B-b)>=a) and (a!=n and b!=n):
      b = b+a
      a = 0
      print(min, '>', max)
      continue
    if (B-b)<a and (a!=n and b!=n):
      b = B
      a = a-(B-b)
      print(min, '>', max)
      continue
    if b==B and (a!=n and b!=n):
      b = 0
      print(max, '>')
      continue
    if a!=A and b!=B and b-(A-a)==n and (a!=n and b!=n):
      b = b - (A-a)
      a = A
      print(max, '>', min)
      continue
    else:
      break
else:
  print('impossible')
