n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(n):
    cur = arr[i]
    for j in range(i + 1,n):
        if cur != arr[j]:
            result += 1
            
            
print(result)