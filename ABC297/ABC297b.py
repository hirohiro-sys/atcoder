s = input()
n = (s.rfind("B")-s.find("B"))%2==1
m = s.find("R")<s.find("K")<s.rfind("R")
if n and m: print("Yes")
else: print("No")