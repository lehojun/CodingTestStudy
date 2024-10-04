food_times = list(map(int,input().split()))
k = int(input())

time = 0
i = 0
n = len(food_times)
while(time < k):
    if food_times[i % n] != 0:
        time += 1
        i -= 1
    else:
        continue
    i += 1
    
print(i + 1)