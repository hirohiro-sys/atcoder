n = int(input())
li = list(map(int,input().split()))
new_li = sorted(li)
print(li.index(new_li[-2])+1)