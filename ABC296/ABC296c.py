a,b = map(int,input().split())
A = list(map(int,input().split()))
A_set = set(A)
for i in A_set:
  if i+b in A_set:
    print("Yes")
    exit() #breakだとforから抜けるだけだけどexitはプログラムを終了できる
print("No")