# 1. Найдите сумму цифр трехзначного числа.
n = input('введите трехзначное число')
n = int(n)
c = n % 10
n = n//10
b = n%10
a = n//10
print(a+b+c)
