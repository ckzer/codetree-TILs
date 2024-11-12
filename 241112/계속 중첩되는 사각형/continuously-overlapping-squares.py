OFFSET=100
RANG=201
n=int(input())
li=[[0]*RANG for _ in range(RANG)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if i%2==0:
        color=1
    else:
        color=2
    for x in range(x1+OFFSET, x2+OFFSET):
        for y in range(y1+OFFSET, y2+OFFSET):
            li[x][y]=color

cnt=0
for x in range(RANG):
    for y in range(RANG):
        if li[x][y]==2:
            cnt+=1
print(cnt)