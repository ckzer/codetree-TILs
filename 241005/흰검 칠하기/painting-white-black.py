n=int(input())
OFFSET=100000
check=[[0, 0] for _ in range(OFFSET*2+1)] #왼쪽이 흰, 오른쪽 검
color=[0]*(2*OFFSET+1)  #검정색은 2, 흰색은 1
now = OFFSET
for i in range(n):
    x, direction = input().split()
    x=int(x)
    if direction=='L':  #흰색
        for j in range(now, now-x, -1):
            if check[j][0]>=2 and check[j][1]>=2:
                continue
            check[j][0]+=1
            color[j]=1
        now-=x-1
    elif direction=='R':    #검정색
        for j in range(now, now+x):
            if check[j][0]>=2 and check[j][1]>=2:
                continue
            check[j][1]+=1
            color[j]=2
        now+=x-1

black, white, grey = 0, 0, 0
for i in range(200001):
    if check[i][0]>=2 and check[i][1]>=2:
        grey+=1
    else:
        if color[i]==2:
            black+=1
        elif color[i]==1:
            white+=1
print(white, black, grey)