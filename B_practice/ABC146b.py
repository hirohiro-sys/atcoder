n = int(input())
s = input()
re = ""
for i in range(len(s)):
  if ord(s[i])+n<=90:
    re+=chr(ord(s[i])+n)
  elif ord(s[i])+n>90:
    re+=chr(ord(s[i])+n-26)
print("".join(re))