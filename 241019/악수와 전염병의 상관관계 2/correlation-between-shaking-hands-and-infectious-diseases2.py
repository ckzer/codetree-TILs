N, K, P, T = map(int, input().split())

arr = []
for _ in range(T):
    t, x, y = map(int, input().split())
    arr.append((t, x, y))

infected = [False]*(N+1)
infected[P] = True
shake_num = [0]*(N + 1)

arr.sort(key=lambda x: x[0])

for t, x, y in arr:
    if infected[x]:
        shake_num[x]+=1
    if infected[y]:
        shake_num[y]+=1

    if shake_num[x]<=K and infected[x]:
        infected[y]=True
    if shake_num[y]<=K and infected[y]:
        infected[x]=True

for i in range(1, N+1):
    print(1 if infected[i] else 0, end="")