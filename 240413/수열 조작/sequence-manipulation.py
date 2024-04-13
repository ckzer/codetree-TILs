from collections import deque
dq=deque()
n=int(input())
for i in range(1, n+1):
    dq.append(i)
for i in range(n-1):
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])

# time complextiy : O(N)