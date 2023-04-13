n = int(input())
s = input()
max_list = [0]
x = 0
for i in s:
  if i=="I":
    x+=1
    max_list.append(x)
  elif i=="D":
    x-=1
    max_list.append(x)
print(max(max_list))