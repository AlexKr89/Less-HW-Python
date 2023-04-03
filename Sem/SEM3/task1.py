# a = [1, 2, 7, 8, 7, 9, 7, 8]
# b = set(a)
# print(len(set(a)))
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = (int(input("Введите число сдвига: ")))
# print(a[-k:] + a[:-k])

list = [1, 1, 3, 4, 5, 6, 7, 8, 9, 3]
count = 0
for i in range (1,len(list)):
    if list[i] > list[i-1]:
        count += 1
print(count)


