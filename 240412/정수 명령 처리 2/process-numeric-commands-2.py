from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
    
    def push(self, item):
        self.dq.append(item)

    def empty(self):
        if not self.dq:
            return 1
        return 0

    def pop(self):
        if self.empty():
            return 1
        return self.dq.popleft()
    
    def size(self):
        return len(self.dq)
    
    def front(self):
        if self.empty():
            return 1
        return self.dq[0]

q=Queue()
n=int(input())
for i in range(n):
    a=input().split()
    if a[0]=='push':
        q.push(a[1])
    elif a[0]=='pop':
        print(q.pop())
    elif a[0]=='empty':
        print(q.empty())
    elif a[0]=='size':
        print(q.size())
    else:
        print(q.front())