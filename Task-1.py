"""Найдите сумму цифр трехзначного числа.Пример:
123 -> 6 (1 + 2 + 3)100 -> 1 (1 + 0 + 0)
"""


number = int(input('Введите целоe, положительное, трехзначное число: '))
element1 = number // 100
element2 = number // 10 % 10
element3 = number % 10
summ = element1 + element2 + element3
print(
    f'Сумма цифр в числе {number} составляет -> {summ} ({element1}+{element2}+{element3})')