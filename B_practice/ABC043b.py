s = input()
li = []
for i in s:
  if i=="0":
    li.append("0")
  elif i=="1":
    li.append("1")
  else:
    if li:
      li.pop()
print(''.join(li))