# Выведите на экран все числа в диапазоне от 1 до 100 кратные 7.
for i in range(1, 101):
    if i % 7:
        pass
    else:
        print(i)
# факториал числа
n = int(input())
q = 1
for i in range(1, n + 1):
    q *= i
print(q)
# Напечатайте таблицу умножения на 5. Предпочтительно печатать 1 x 5
# = 5, 2 x 5 = 10, а не просто 5, 10 и т. д
q = 0
N = int(input())
for i in range(N + 1):
    n = i * 5
    print(q, "x", 5, "=", n)
    q += 1
# Дан список [0,5,2,4,7,1,3,19]. Написать программу для подсчета нечетных цифр в нем.
list_1 = [0, 5, 2, 4, 7, 1, 3, 19]
count = 0
for i in list_1:
    if i % 2:
        count += 1
    else:
        pass
print(count)
# список случайных чисел
import random
randlist = []
for i in range(4):
    randlist.append(random.randint(0, 20))
list_1 = randlist[:4]
for i in (list_1):
    i = int(i)
    i *= 2
    randlist.append(i)
print(randlist)
# Создайте список из 12 элементов. Каждый элемент этого списка представляет собой
# зарплату рабочего за месяц (случайное число от 7500 до 15000 грн.). Выведите этот
# список на экран и вычислите среднемесячную зарплату этого рабочего.\
salary = []
for i in range(12):
    salary.append(random.randint(7500, 15000))
print(salary)
print(sum(salary) / 12)
# Представьте в виде списка списков матрицу
# [ 1, 2 , 3, 4]
# [ 5, 6 , 7, 8]
# [ 9,10, 11, 12]
# [13,14, 15, 16]
a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]
print(a[0], a[1], a[2], a[3], sep="\n")
# Напишите программу, которая выведет эту матрицу на экран, вычислит и выведет
# сумму элементов этой матрицы.
print(sum(a[0]) + sum(a[1]) + sum(a[2]) + sum(a[3]))
# Написать код для зеркального переворота списка [7,2,9,4] -> [4,9,2,7].
# Список может быть произвольной длины. (При выполнении задания
# использовать дополнительный список нельзя)
m = list(input())
m.reverse()
print(m)
#С помощью циклов вывести на экран все простые числа от 1 до 100.
for num in range(2,101):
    if num%num==0 and num%2!=0 and num%3!=0 and num%4!=0 and num%5!=0 and num%6!=0 and num%7!=0 and num%8!=0 and num%9!=0:
        print("prime number",num)
    else:
        print("not prime number",num)
# another solution
list = []
for i in range(1, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list.append(i)
print(list)
