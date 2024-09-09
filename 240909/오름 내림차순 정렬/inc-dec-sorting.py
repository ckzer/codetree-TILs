n=int(input())
li=list(map(int, input().split()))
li.sort()
for i in li:
    print(i, end=' ')
print()
li.sort(reverse=True)
for i in li:
    print(i, end=' ')