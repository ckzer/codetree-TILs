n=int(input())
rectangle=[[0]*201 for _ in range(201)]
li=[]
for i in range(n):
    li.append(list(map(int, input().split())))
for x, y in li:
    for i in range(8):
        for j in range(8):
            rectangle[x+i][y+j]=1

sum=0
for i in range(201):
    for j in range(201):
        if rectangle[i][j]==1:
            sum+=1
print(sum)