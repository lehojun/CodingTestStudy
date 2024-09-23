m = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)
arr.append(0)

result = 0
cnt = arr[0]

for i in arr:
    if cnt != 0:
        cnt -= 1
    elif cnt == 0:
        result += 1
        cnt = i
        cnt -= 1
    
print(result)
