w,a,b = map(int,input().split())
if b+w<=a:
  print(abs(b+w-a))
elif w+a>=b:
  print(0)
else:
  print(abs(w+a-b))