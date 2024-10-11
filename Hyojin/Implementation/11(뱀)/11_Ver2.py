n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
info = [] # 회전 방향 정보

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1
    
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x, y = 1, 1
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 # 처음에 동쪽을 보고 있음
    time = 0
    index = 0 # 다음에 회전할 정보
    q = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 맵 범위 안에 있고 뱀의 몸통이 없는 위치라면
        if 1 <= nx and nx <= n and 1<= ny and ny<= n and data[nx][ny] !=2 :
            # 사과가 없다면 이동 후 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px, py = q.pop()
                data[px][py] = 0
            # 사과가 있다면 이동 후 꼬리 그대로
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < 1 and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1           
    return time
                
print(simulate())