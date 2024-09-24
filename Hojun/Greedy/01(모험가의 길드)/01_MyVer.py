n = int(input())
m = list(map(int, input().split()))
m.sort()

group = 0
member = 0

for i in m:
  member += 1
  if member >= i:
    group += 1
    member = 0

print(group)
