N = int(input())
a = []
b = []
T = [[] for i in range(N)]
for i in range(N-1):
  A,B = map(int,input().split())
  a.append(A)
  b.append(B)
for i in range(N-1):
  T[a[i]-1].append(b[i])
  T[b[i]-1].append(a[i])
for i in range(N):
  if len(T[i]) == N-1:
    print("Yes")
    exit()
print("No")  