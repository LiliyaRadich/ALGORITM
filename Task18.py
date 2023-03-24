import random

number = int(input('введите длину списка: '))
my_list = [random.randint(0, 100) for _ in range(number)]
print(my_list)
my_list.sort()
print(my_list)
find = int(input('какое число ищем?: '))
count = 0
i = 0
dig_min = 0
dig_max = 0
for date in my_list:
    if date == find:
        count += 1
        print(f'Число {find} встречается в списке {count} раз')
for date in my_list:
    if my_list[i] < find:
        dig_min = my_list[i]
        i += 1
for date in my_list:
    if my_list[i] > find:
        dig_max = my_list[i]
        i += 1
    break
if abs(dig_min - find) < abs(dig_max - find):
    print(f'Максимально близкое число от {find} -> {dig_min}')
else:
    print(f'Максимально близкое число от {find} -> {dig_max}')
