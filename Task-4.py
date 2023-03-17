"""Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
Пример:3 2 4 -> yes
3 2 1 -> no"""

choco_size1 = int(input('Введите первый размер шоколадки: '))
choco_size2 = int(input('Введите второй размер шоколадки: '))
cut = int(input('Сколько долек нужно отломить от шоколадки? '))
if cut < choco_size1 * choco_size2 and cut % choco_size1 == 0 or cut % choco_size2 == 0:
    print(f'{choco_size1} {choco_size2} {cut} -> yes')
else:
    print(f'{choco_size1} {choco_size2} {cut} -> no')