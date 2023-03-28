# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,# и возводит число А в целую степень B с помощью рекурсии.
## *Пример:*
## A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
num = int(input('Введите число: '))stepen = int(input('Введите степень: '))

def stepen_znach(date, step):    if step == 1:
        return date    else:
        return (date * stepen_znach(date, step - 1))
print(f'Число {num} в степене {stepen} = {stepen_znach(num, stepen)}')