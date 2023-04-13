n = int(input())
li = list(map(int,input().split()))
m = int(input())
for _ in range(m):
  a,b = map(int,input().split())
  s = li[a-1]
  li[a-1] = b
  print(sum(li))
  li[a-1] = s