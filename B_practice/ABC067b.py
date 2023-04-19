n,k = map(int,input().split())
li = list(map(int,input().split()))
li = sorted(li, reverse=True)
re = 0
count = 0
for i in li:
  re += i
  count += 1
  if count == k:
    break
print(re)