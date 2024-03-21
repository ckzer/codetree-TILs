import sys
n=int(input())
li=list(map(int, input().split()))
final_min=sys.maxsize
for i in range(n):
    each_sum=0
    for j in range(i):
        each_sum+=(i-j)*li[j]
    for k in range(i+1, n):
        each_sum+=(k-i)*li[k]
    if final_min>each_sum:
        final_min=each_sum
print(final_min)