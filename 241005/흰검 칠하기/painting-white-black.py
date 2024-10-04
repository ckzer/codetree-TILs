n=int(input())
check=[0]*200001
color=[0]*200001    #검정색은 2, 흰색은 1
now = 100000
for i in range(n):
    x, direction = input().split()
    x=int(x)
    if direction=='L':  
        for j in range(now, now-x, -1):
            if color==1:
                continue
            check[j]+=1
            color[j]=1
        now-=x-1
    elif direction=='R':
        for j in range(now, now+x):
            if color==2:
                continue
            check[j]+=1
            color[j]=2
        now+=x-1

black, white, grey = 0, 0, 0
for i in range(200001):
    if check[i]>=4:
        grey+=1
    else:
        if color[i]==2:
            black+=1
        elif color[i]==1:
            white+=1
print(white, black, grey)