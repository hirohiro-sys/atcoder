s = input()
count = 0
if s[0]==s[1]==s[2]==s[3]:
  print("Weak")
  exit()
for i in range(len(s)-1):
  if int(s[i+1])-int(s[i])==1 or abs(int(s[i+1])-int(s[i]))==9:
    count += 1

if count==3:
  print("Weak")
else:
  print("Strong")