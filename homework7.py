# Напишите программу, которая посчитает сколько букв «b» в введенной
# строке текста.
n = input()
count = 0
for i in n:
    if i == "b":
        count += 1
print(count)
# Считайте строку, которая будет представлять имя человека, введенное с
# клавиатуры. Проверьте эту строку на валидность. Имеется в виду, что
# например, в имени человека не может быть цифр, оно должно
# начинаться с большой буквы, за которой должны следовать маленькие.
name = input("input your name ")
if name[0].isupper() and name[1:].islower():
    for element in (name):
        if element.isdigit():
            print("try again")
            break
    else:
        print(name)
else:
    print("Enter your name again")
# Вводится строка из слов, разделенных пробелами. Найти самое длинное
# слово и вывести его на экран
n = input("Введите ваш текст: ")
s = n.split()
print(max(s, key=len))
# Выведите на экран 10 строк со значением числа Pi. В первой строке
# должно быть 2 знака после запятой, во второй 3 и так далее.
import math

for i in range(2, 12):
    n = "{:." + str(i) + "f}"
    print(i - 1, n.format(math.pi))
# Напишите программу, которая вычислит сумму всех кодов символов строки.
n = input("Введите текст: ")
sum = 0
for i in n:
    sum += ord(i)
print(sum)
n=input()
# скрипт для удаления тегов
n=input()
n=n.split()
# <p> <b> Для длинных цитат браузер вставляет </b> отступы со всех сторон. </b> ( рабочий пример пример)
# можно вставлять любой тег.единственное, должны быть разделены пробелами
number=int(input("input how many teg you want to delete"))
for _ in range(number):
    N=input("which teg you want to delete")
    while N in n:
        for element in (n):
            if element==N:
                n.remove(N)
n=" ".join(n)
print(n)
