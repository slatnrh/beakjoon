import sys
input = sys.stdin.readline

# spread: 1초 뒤 미세먼지 확산 현황
def spread():
    dx = [1, -1, 0, 0]    
    dy = [0, 0, 1, -1]

    tmp_lst = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if lst[i][j] != 0 and lst[i][j] != -1:
                tmp = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < R and 0 <= ny < C and lst[nx][ny] != -1:
                        tmp_lst[nx][ny] += lst[i][j] // 5
                        tmp += lst[i][j] // 5
                lst[i][j] -= tmp
    
    for i in range(R):
        for j in range(C):
            lst[i][j] += tmp_lst[i][j]

# 공기청정기 위쪽 공기 흐름
def cleaner_up_air():
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = cleaner_top, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == cleaner_top and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        lst[x][y], before = before, lst[x][y]
        x = nx
        y = ny

# 공기청정기 아래쪽 공기 흐름
def cleaner_down_air():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    direct = 0
    before = 0
    x, y = cleaner_bottom, 1
    while True:
        nx = x + dx[direct]
        ny = y + dy[direct]
        if x == cleaner_bottom and y == 0:
            break
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            direct += 1
            continue
        lst[x][y], before = before, lst[x][y]
        x = nx
        y = ny

R, C, T = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(R)]

cleaner_top = -1
cleaner_bottom = -1

# 공기청정기 위치 찾기
for i in range(R):
    if lst[i][0] == -1:
        cleaner_top = i
        cleaner_bottom = i + 1
        break

for _ in range(T):
    spread()
    cleaner_up_air()
    cleaner_down_air()

# T초 뒤 미세먼지 총량 구하기
rslt = 0
for i in range(R):
    for j in range(C):
        if lst[i][j] > 0:
            rslt += lst[i][j]

print(rslt)