import math
a,b = input().split()
s = int(a+b)
if math.sqrt(s).is_integer():
  print("Yes")
else:
  print("No")