# Задача 16: Требуется вычислить, сколько раз встречается 
# некоторое число X в массиве A[1..N]. Пользователь 
# в первой строке вводит натуральное число N – количество 
# элементов в массиве. В последующих  строках записаны 
# N целых чисел Ai. Последняя строка содержит число X


n = int(input("Количество элементов в массиве: "))
a = []
for i in range(n):
    a.insert(i, int(input("Введите элемент массива: ")))
x = int(input("Введите число для проверки: "))
count = 0
for el in a:
    if el == x:
        count +=1
print(count)