# Задача 32: Определить индексы элементов массива,
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
array = sorted([random.randint(1, 100)
                for _ in range(10)])

print(array)

minvalue = int(input("Введите минимальное значение: "))
maxvalue = int(input("Введите максимальное значение: "))

indices = []

for i in range(len(array)):
    if array[i] >= minvalue and array[i] <= maxvalue:
        indices.append(i)

print("Индексы элементов массива, значения которых принадлежат заданному диапазону:", indices)
