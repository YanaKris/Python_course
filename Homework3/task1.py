#1 Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит
#натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#Пример:
#5
#1 2 3 4 5
#3
#-> 1
#list_nums = [int(input()) for _ in range(int(input()))] 
#print(list_nums.count(int(input())))
#print(dir(list))
# N = int(input('колличество элементов в массиве '))
# A = list(range(N))
# print(A)
# print(A.count(2))
#list_nums = [int(input()) for _ in range(int(input()))] 

from random import randint

list_nums = [randint(0, 9) for _ in range(int(input()))]

print(list_nums)

print(list_nums.count(int(input())))
