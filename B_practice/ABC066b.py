s = input()
count = 0
for _ in range(len(s)):
  s = s[:-1]
  if len(s)%2==0 and s[:len(s)//2]==s[len(s)//2:]:
    count += len(s)
    print(count)
    exit()