# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def power(A, B):
    if B == 1:
        return(A)
    if B > 1:
        return (A * power(A, B - 1))
A = int(input('число')) 
B = int(input('степень'))   
print(power(A,B))