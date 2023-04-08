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