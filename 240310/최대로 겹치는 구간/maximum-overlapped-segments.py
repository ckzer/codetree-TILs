n=int(input())
li=[0]*201
for i in range(n):
    a, b=tuple(map(int, input().split()))
    for j in range(a+100, b+100):
        li[j]+=1
print(max(li))