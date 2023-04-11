s = input()
li = []
for i in s:
  li.append(i)
for i in s:
  if li.count(i)%2==0:
    continue
  else:
    print("No")
    exit()
print("Yes")