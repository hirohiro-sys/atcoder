al = "abcdefghijklmnopqrstuvwxyz"
S = set(input())
for s in al:
  if s not in S:
    print(s)
    exit()
print("None")