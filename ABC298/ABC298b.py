N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

for _ in range(4):
    ans = True
    A = list(zip(*A))[::-1]        #90度反転
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] == 0:
                ans = False
    if ans:
        print('Yes')
        exit()
print('No')