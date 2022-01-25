# счастливый билет.проверить является ли шестизначный билет счастливым.Если получится не привязыватся к
# номеру билета выполнить код
# 6-ти значный билет
g = list(map(int,input("enter your ticket")))
if g[0] + g[1] + g[2] == g[3] + g[4] + g[5]:
    print("your ticket is lucky")
else:
    print("You have a regular ticket")
# Любой билет
f = list(map(int,input("enter your ticket")))
h = len(f) // 2
if sum(f[0:h]) == sum(f[h:]):
    print("your ticket is lucky")
else:
    print("You have a regular ticket")
# число палиндром.Для начала разберемся с 6-ти значным числом
n = list(map(int,input("enter a number")))
j = n[::-1]
if n[0:3] == j[0:3]:
    print("число не полиндром")
else:
    print("вы ввели простое число")
# программа,которая работает с любым числом.Другим способом.
n = list(map(int,input("enter a number")))
u = len(n) // 2
k = n[::-1]
if n[0:u] == k[0:u]:
    print("Число является полиндромом", n)
else:
    print("число не полиндром", n)
# круг, не уверен
x = float(input("Введите координаты точки x: "))
y = float(input("Введите координаты точки y: "))
R = 4
if (x - 0) ** 2 + (y - 0) ** 2 <= R ** 2:
    print("Точка находится в кругу")
else:
    print("Точка за пределами круга")
