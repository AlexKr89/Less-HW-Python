# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

numN = int(input("Введите число N: "))

for i in range(numN+1):
    print(2**i)