# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.# Выведите минимальное количество монет, которые нужно перевернуть\

import random

number = int(input('Введите количество монет: '))
count_1 = 0
count_2 = 0
temp = 0
for i in range(number):
    temp = random.randint(0, 1)
    if temp == 0:
        count_1 += 1 else:
        count_2 += 1
        print(count_1, count_2)
if count_1 > count_2:
    print(count_2) else:
    print(count_1)
