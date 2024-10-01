n, m = map(int, input().split())
arr = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i + 1,n):
        if arr[i] != arr[j]:
            result += 1
            
            
print(result)