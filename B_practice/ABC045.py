sa = list(input())
sb = list(input())
sc = list(input())
n = "a"
while True:
  if n=="a":
    if sa:
      n = sa.pop(0)
    else:
      result = "A"
      break
  elif n=="b":
    if sb:
      n = sb.pop(0)
    else:
      result = "B"
      break
  elif n=="c":
    if sc:
      n = sc.pop(0)
    else:
      result = "C"
      break
print(result)