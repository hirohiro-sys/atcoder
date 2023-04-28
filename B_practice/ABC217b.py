a = input()
b = input()
c = input()
li = [a,b,c]
li2 = ['ABC' , 'ARC' , 'AGC' , 'AHC']
for i in li2:
  if i not in li:
    print(i)
    exit()