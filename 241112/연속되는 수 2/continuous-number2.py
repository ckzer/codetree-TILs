n=int(input())
max_cnt=0
cnt=0
for i in range(n):
    num=int(input())
    if i==0 or num_before!=num:
        if cnt>max_cnt:
            max_cnt=cnt
        cnt=1
    else:
        cnt+=1
print(cnt)