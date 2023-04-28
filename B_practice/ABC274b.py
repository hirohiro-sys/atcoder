h,w = map(int,input().split())
li = [input() for i in range(h)]
for i in range(len(li[0])):
  count = 0
  for j in range(len(li)):
    if li[j][i]=="#":      #もし列から二次元配列を見る時はリスト参照に注意
      count += 1
  print(count,end=" ")