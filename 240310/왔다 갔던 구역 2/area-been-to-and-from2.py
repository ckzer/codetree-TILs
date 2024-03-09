n=int(input())
li=[0]*2000
segment=[
    input().split()
    for _ in range(n)
]
now=1000
for x, direction in segment:
    if direction=='L':
        for j in range(int(x)):
            li[now]+=1
            now+=1
    elif direction=='R':
        for j in range(int(x)):
            now-=1
            li[now]+=1
cnt=0
for i in range(2000):
    if li[i]>1:
        cnt+=1
print(cnt)