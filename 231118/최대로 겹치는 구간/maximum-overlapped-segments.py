n=int(input())
li=[tuple(map(int, input().split())) for _ in range(n)]
li_range=[0]*200
for x1, x2 in li:
    for i in range(x1, x2):
        li_range[i+100]+=1
print(max(li_range))