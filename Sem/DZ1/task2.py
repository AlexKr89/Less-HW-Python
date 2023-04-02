# Найдите сумму цифр трехзначного числа.

num = int(input("Введите трехзначное число: "))

if num%100==0:
    sum = num//100
elif num%10==0:
    sum = num//100 + num//10%10
else:
    sum = num%10 + num//100 + num//10%10

print(sum)