n=int(input())
white=0
black=0

for i in range(n):
    x, direction = input().split()
    x=int(x)
    if direction=='L':
        white+=x
        black-=x
        if black<0:
            black=0
    else:
        black+=x
        white-=x
        if white<0:
            white=0
print(white, black)