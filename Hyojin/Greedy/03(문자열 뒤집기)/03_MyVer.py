data = input()

n = 0
m = 0

if data[0] == '0':
    n += 1
elif data[0] == '1':
    m += 1
    
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        if data[i + 1] == '0':
            n += 1
        else:
            m += 1
            
print(min(n, m))