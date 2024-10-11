n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)]
moveList = []

for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1
    
l = int(input())
for _ in range(l):
    x, c = input().split()
    moveList.append((int(x), c))
    
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

time = 0
x, y = 1, 1 # 뱀 머리의 위치
data[x][y] = 2 # 뱀 몸이 존재하는 곳
idx = 0 # 방향 인덱스 처음에는 0
flag = True
s = [(x,y)]
for i in range(l):
    t = moveList[i][0]
    c = moveList[i][1]
    for j in range(t):
        preX = x
        preY = y
        x += dx[idx]
        y += dy[idx]
        time += 1
        # 벽을 넘을 경우
        if x < 1 or x > n or y < 1 or y > n:
            flag = False
            break
        # 몸이랑 닿았을 경우
        if data[x][y] == 2:
            flag = False
            break
        # 사과가 없다면
        if data[x][y] == 0:
            data[x][y] = 2
            s.append((x,y))
            px, py = s.pop()
            data[px][py] = 0
        # 사과가 있다면
        if data[x][y] == 2:
            data[x][y] = 2
            s.append((x,y))
    if flag == False:
        break
    if c == 'L':
        idx = (idx - 1) % 4
    else:
        idx = (idx + 1) % 4
        
print(time)
     
    