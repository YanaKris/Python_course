# 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
s = input('введите номер билета')
s = int(s)
n = s % 1000
c = n % 10
n = n // 10
b = n % 10
a = n // 10
n = a+b+c
n1 = s // 1000
c1 = n1 % 10
n1= n1 // 10
b1 = n1 % 10
a1 = n1 // 10
n1 = a1+b1+c1
if n == n1:
    print('cчастливый')
else:
    print('no')
