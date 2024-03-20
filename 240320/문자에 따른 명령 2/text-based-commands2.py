x, y=0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir = 3
move=input()
for i in range(len(move)):
    if move[i]=='L':
        dir=(dir+3)%4
    elif move[i]=='R':
        dir=(dir+1)%4
    else:
        x, y = x+dx[dir], y+dy[dir]
print(x, y)