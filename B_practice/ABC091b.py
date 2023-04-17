n = int(input())
s = [input() for i in range(n)]
s2 = list(set(s))
m = int(input())
t = [input() for i in range(m)]
ans = 0
for i in range(0,len(s2)):
  ans = max(ans,s.count(s2[i]) - t.count(s2[i]))
print(ans)