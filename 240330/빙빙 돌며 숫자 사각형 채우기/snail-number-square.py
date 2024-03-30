n, m = map(int, input().split())
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
rectangle = [
    [0] * m for _ in range(n)
]
direction = 0
dx, dy = 0, 0
x, y = 0, 0
rectangle[0][0]=1
def inRange(dx, dy):
    return 0<=dx<n and 0<=dy<m

for i in range(2, n*m+1):
    dx, dy = x+dxs[direction], y+dys[direction]
    if inRange(dx, dy) and rectangle[dx][dy]==0:
        pass
    else:
        direction=(direction+1)%4
    x, y = x+dxs[direction], y+dys[direction]
    rectangle[x][y]=i

for i in range(n):
    for j in range(m):
        print(rectangle[i][j], end=' ')
    print()