n = int(input())
count1 = count2 = 0
for i in range(n):
    num = int(input())
    if num:
        count1 += 1
    else:
        count2 +=1

if count1 > count2:
    print(count1)
else:
    print(count2)