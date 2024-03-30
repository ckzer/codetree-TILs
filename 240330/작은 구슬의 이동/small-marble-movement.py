n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
direction={
    'U' : 2,
    'D' : 1,
    'R' : 0,
    'L' : 3
}
moveDir=direction[d]

def isRange(x, y):
    return 1<=x<=n and 1<=y<=n

for i in range(t):
    r, c = r+dxs[moveDir], c+dys[moveDir]
    if not isRange(r, c):
        r, c = r-dxs[moveDir], c-dys[moveDir]
        moveDir = 3 - moveDir

print(r, c)