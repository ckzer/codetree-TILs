n, k=map(int, input().split())
li=[0 for _ in range(n+1)]

for i in range(k):
    a, b=map(int, input().split())
    for j in range(a, b+1):
        li[j]+=1
print(max(li))