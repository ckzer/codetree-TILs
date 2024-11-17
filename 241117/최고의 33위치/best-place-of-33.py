n=int(input())
li=[list(map(int, input().split())) for _ in range(n)]
max_cnt=0
for i in range(n-2):        #행
    for j in range(n-2):    #열
        cnt=0
        for x in range(3):
            for y in range(3):
                cnt+=li[i+x][j+y]
        if max_cnt<cnt:
            max_cnt=cnt
print(max_cnt)