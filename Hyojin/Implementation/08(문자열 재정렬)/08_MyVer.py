s = input()

arr = []
sum = 0

for i in s:
    if i.isdigit():
        sum += int(i)
    else:
        arr.append(i)
        
arr.sort()

for i in arr:
    print(i, end = "")
print(sum)