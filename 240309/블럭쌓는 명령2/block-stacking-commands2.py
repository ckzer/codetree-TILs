n, k=tuple(map(int, input().split()))
li=[0]*(n)
for i in range(k):
    a, b=map(int, input().split())
    for j in range(a-1, b):
        li[j]+=1
print(max(li))