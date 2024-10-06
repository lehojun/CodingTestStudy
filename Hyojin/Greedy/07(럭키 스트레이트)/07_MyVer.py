score = input()

len = len(score)

sum1 = 0
for i in range(0, len // 2):
    sum1 += int(score[i])
    
sum2 = 0
for i in range(len // 2, len):
    sum2 += int(score[i])
    
    
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")