# n, m=map(int, input().split())
# li1=[]
# li2=[]

# now=0
# check=False
# for i in range(n):
#     direction, num=input().split()
#     num=int(num)
#     for j in range(num):
#         if direction=='L':
#             now-=1
#             li1.append(now)

#         elif direction=='R':
#             now+=1
#             li1.append(now)
    
# now=0
# for i in range(m):
#     direction, num=input().split()
#     num=int(num)
#     for j in range(num):
#         if direction=='L':
#             now-=1
#             li2.append(now)

#         elif direction=='R':
#             now+=1
#             li2.append(now)

# for i in range(len(li1) if len(li1)>len(li2) else len(li2)):
#     if li1[i]==li2[i]:
#         check=True
#         print(i+1)
#         break
# if check==False:
#     print(-1)
MAX_T = 1000000

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

# A가 매 초마다 서있는 위치를 기록
time_a = 1
for _ in range(n):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1

# B가 매 초마다 서있는 위치를 기록
time_b = 1
for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1

# 최초로 만나는 시간을 구합니다.
ans = -1
for i in range(1, time_a):
    if pos_a[i] == pos_b[i]:
        ans = i
        break
        
print(ans)