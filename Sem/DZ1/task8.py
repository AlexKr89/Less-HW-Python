# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек.
# Разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

num1 = int(input("Введите количество долек по одной стороне шоколадки: "))
num2 = int(input("Введите количество долек по другой стороне шоколадки: "))
num3 = int(input("Сколько долек вы хотите отломить: "))


if (num3%num1==0 or num3%num2==0) and num3<=num1*num2:
    print("yes")
else:
    print("no")