h,w = map(int,input().split())
print("#"*w+"##")
for _ in range(h):
  s = input()
  print("#"+s+"#")
print("#"*w+"##")