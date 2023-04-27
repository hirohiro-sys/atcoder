s = input()
s2 = s[::-1]
count = 0
for i in range(len(s)):
  if s[i]!=s2[i]:
    count+=1
print(count//2)