n,t = map(int,input().split())
c = list(map(int,input().split()))
r = list(map(int,input().split()))
li = []
li2 = []
for i in range(len(c)):
  if c[i-1]==t:
    li.append(r[i-1])

if len(li)>=1:
  print(r.index(max(li))+1)
  exit()
  

for i in range(len(c)):
  if c[i-1]==c[0]:
    li2.append(r[i-1])
print(r.index(max(li2))+1)