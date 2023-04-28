h,w = map(int,input().split())
li = [input() for i in range(h)]
for i in range(len(li[0])):
  count = 0
  for j in range(len(li)):
    if li[j][i]=="#":      #今回は二次元配列を列から見てるからj→iの順番で参照
      count += 1
  print(count,end=" ")
