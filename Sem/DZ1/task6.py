# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

num = int(input("Введите шестизначный номер вашего билета: "))

firstHalf = int(num//100000 + num//10000%10 + num//1000%10)
secondHalf = int(num//100%10 + num//10%10 + num%10)

if firstHalf == secondHalf:
    print("yes")
else:
    print("no")