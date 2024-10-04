n=int(input())
li=[0]*2000
now=1000
for i in range(n):
    x, direction = input().split()
    x=int(x)
    if direction=='L':
        for j in range(now, now-x, -1):
            li[j]+=1
        now-=x
    elif direction=='R':
        for j in range(now, now+x):
            li[j]+=1
        now+=x

cnt=0
for i in li:
    if i>=2:
        cnt+=1
print(cnt)