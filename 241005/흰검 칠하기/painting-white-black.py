n = int(input())
OFFSET = 100000
MAX_RANGE = 200000  # 충분한 범위로 설정

check = [0] * (2 * OFFSET + 1)  # 타일 칠해진 횟수 추적
color = [0] * (2 * OFFSET + 1)  # 현재 타일 색깔 저장 (0: 없음, 1: 흰색, 2: 검은색)
now = OFFSET  # 현재 위치 (OFFSET을 중심으로 이동)

for i in range(n):
    x, direction = input().split()
    x = int(x)
    if direction == 'L':
        for j in range(now, now - x, -1):
            if check[j] >= 2:
                continue  # 이미 회색으로 바뀐 경우 더 이상 변경하지 않음
            if color[j] != 0 and color[j] != 1:  # 색이 덮어씌워지는 경우
                check[j] += 1
            color[j] = 1  # 흰색으로 색칠
        now -= x  # 왼쪽으로 x칸 이동
    elif direction == 'R':
        for j in range(now, now + x):
            if check[j] >= 2:
                continue  # 이미 회색으로 바뀐 경우 더 이상 변경하지 않음
            if color[j] != 0 and color[j] != 2:  # 색이 덮어씌워지는 경우
                check[j] += 1
            color[j] = 2  # 검은색으로 색칠
        now += x  # 오른쪽으로 x칸 이동

black, white, grey = 0, 0, 0

for i in range(2 * OFFSET + 1):
    if check[i] >= 2:
        grey += 1
    elif color[i] == 1:
        white += 1
    elif color[i] == 2:
        black += 1

print(white, black, grey)