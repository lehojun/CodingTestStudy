n = list(map(int,input()))
result = 0

for i in range(len(n)-1):
  if n[i] == 0 and n[i+1] == 1:
      result +=1

print(result)
