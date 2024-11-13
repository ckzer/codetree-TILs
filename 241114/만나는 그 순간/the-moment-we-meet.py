n, m=map(int, input().split())
li1=[]
li2=[]

now=0
check=False
for i in range(n):
    direction, num=input().split()
    num=int(num)
    for j in range(num):
        if direction=='L':
            now-=1
            li1.append(now)

        elif direction=='R':
            now+=1
            li1.append(now)
    
now=0
for i in range(m):
    direction, num=input().split()
    num=int(num)
    for j in range(num):
        if direction=='L':
            now-=1
            li2.append(now)

        elif direction=='R':
            now+=1
            li2.append(now)

for i in range(len(li1) if len(li1)>len(li2) else len(li2)):
    if li1[i]==li2[i]:
        check=True
        print(i+1)
        break
if check==False:
    print(-1)
