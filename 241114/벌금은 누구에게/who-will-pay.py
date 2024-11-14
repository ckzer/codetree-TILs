n, m, k=map(int, input().split())
student=[0]*(n+1)
check=False
for i in range(m):
    cnt=int(input())
    student[cnt]+=1
    if student[cnt]==k:
        check=True
        check_num=cnt
        break
print(check_num if check else -1)