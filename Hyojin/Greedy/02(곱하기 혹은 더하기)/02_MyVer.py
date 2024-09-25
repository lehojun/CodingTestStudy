s = input()

result = int(s[0])
    
for i in range(1, len(s)):
    if result == 0:
        print(i)
        result += int(s[i])
    else:
        print('*: ', i)
        result *= int(s[i])
        
print(result)