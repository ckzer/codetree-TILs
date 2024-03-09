n=int(input())
li = [0]*100
for i in range(n):
    a, b=tuple(map(int, input().split()))
    for j in range(a-1, b):
        li[j]+=1
print(max(li))