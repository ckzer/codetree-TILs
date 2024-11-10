OFFSET=1000
MAX_RANGE=2001
cnt=0
check=True
li=[[0]*MAX_RANGE for _ in range(MAX_RANGE)]
rect_1=list(map(int, input().split()))
rect_2=list(map(int, input().split()))

for i in range(rect_1[0]+OFFSET, rect_1[2]+OFFSET): # x좌표
    for j in range(rect_1[1]+OFFSET, rect_1[3]+OFFSET): # y좌표
        li[i][j]=1

for i in range(rect_2[0]+OFFSET, rect_2[2]+OFFSET): # x좌표
    for j in range(rect_2[1]+OFFSET, rect_2[3]+OFFSET): # y좌표
        li[i][j]=0

max_x, max_y, min_x, min_y= 0, 0, MAX_RANGE, MAX_RANGE

for x in range(rect_1[0]+OFFSET, rect_1[2]+OFFSET):
    for y in range(rect_1[1]+OFFSET, rect_1[3]+OFFSET):
        if li[x][y]==1:
            check=False
            if x>max_x:
                max_x=x
            if y>max_y:
                max_y=y
            if x<min_x:
                min_x=x
            if y<min_y:
                min_y=y
if check:
    depth=0
else:
    depth=(max_x-min_x+1) * (max_y-min_y+1)
print(depth)