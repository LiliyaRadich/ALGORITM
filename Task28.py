# Задача 28: Напишите рекурсивную функцию sum(a, b),# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.# Также нельзя использовать циклы.
# # *Пример:*# # 2 2
#     4
import random
num1, num2 = [random.randint(0, 100), random.randint(0, 100)]print(num1, num2)

def summa(num_1, num_2):    if num_1 == 0:
        return num_2;    return summa(num_1 - 1, num_2 + 1)
print(f'{num1} + {num2} = {summa(num1, num2)}')