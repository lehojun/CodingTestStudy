n = list(map(int,input()))
result = 1
for i in n:
  if i != 0:
    result *= i
  else:
    result += i

print(result)
