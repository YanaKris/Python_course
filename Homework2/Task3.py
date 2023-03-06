# 3. Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
num =int(input('number'))
count = 1
while num >= count:
    print(count)
    count = count *2
