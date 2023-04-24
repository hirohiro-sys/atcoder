s = input()
tmp = 0
for i in s:
  tmp += int(i)

if int(s)%tmp==0:
  print("Yes")
else:
  print("No")