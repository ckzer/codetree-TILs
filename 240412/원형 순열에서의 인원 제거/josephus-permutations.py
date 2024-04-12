from collections import deque

class Queue:
    def __init__(self):
        self.dq=deque()
    
    def push(self, num):
        self.dq.append(num)
    
    def empty(self):
        return not self.dq

    def pop(self):
        if self.empty():
            raise Exception("empty queue")
        return self.dq.popleft()
    
    def top(self):
        return self.dq[-1]

q=Queue()    
n, k = map(int, input().split())
for i in range(1, n+1):
    q.push(i)
for i in range(n):
    for j in range(k-1):
        q.push(q.pop())
    print(q.pop(), end=' ')