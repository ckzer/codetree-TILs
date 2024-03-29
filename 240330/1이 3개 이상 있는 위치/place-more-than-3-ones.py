n=int(input())
li=[list(map(int, input().split())) for _ in range(n)]

def is_range(dx, dy, n):
    return 0<=dx<n and 0<=dy<n

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
num=0
for i in range(n):
    for j in range(n):
        cnt=0
        for dx, dy in zip(dxs, dys):
            if is_range(i+dx, j+dy, n) and li[i+dx][j+dy]==1:
                cnt+=1
        if cnt>=3:
            num+=1
print(num)