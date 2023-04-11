for i in range(8):
  n = input()
  for j in range(8):
    if n[j]=="*":
      print(chr(97+j)+str(8-i))