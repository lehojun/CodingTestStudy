n = 5
data = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

def possible(answer):
    result = True
    for x, y, stuff in answer:
        if stuff == 0:
            if (y == 0 or [x, y - 1, 0] in answer or [x, y, 1] in answer) == False:
                result = False
        elif stuff == 1:
            if ([x, y - 1, 0] in answer or [x + 1, y -1 , 0] in answer or
                ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer)) == False:
                result = False
                
    return result

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        elif operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
                
    return sorted(answer)
                
print(solution(n, data))
        