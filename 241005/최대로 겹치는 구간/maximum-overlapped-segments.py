OFFSET = 100
n=int(input())
li=[0 for _ in range(201)]
for i in range(n):
    x1, x2 = map(int, input().split())
    for j in range(x1+OFFSET, x2+OFFSET):
        li[j]+=1
print(max(li))