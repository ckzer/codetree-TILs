class Stack:
    def __init__(self):
        self.items=[]
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def empty(self):
        if not self.items:
            return 1
        return 0

    def top(self):
        return self.items[-1]

n=int(input())
s = Stack()
for i in range(n):
    a=input().split()
    if a[0]=='push':
        s.push(int(a[1]))
    elif a[0]=='size':
        print(s.size())
    elif a[0]=='empty':
        print(s.empty())
    elif a[0]=='pop':
        print(s.pop())
    elif a[0]=='top':
        print(s.top())