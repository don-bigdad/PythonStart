# Напишите функцию, которая вернет максимальное число из списка
# чисел.
import random
list=[random.randint(1,101) for _ in range(20)]
def max_element(list):
    return max(list)
    # item=0
    # for element in list:
    #     if element>item:
    #         item=element
    # return item
list=[random.randint(1,101) for _ in range(20)]
print(max_element(list))
print(list)
# Реализуйте функцию, параметрами которой являются - два числа и
# строка. Возвращает она конкатенацию строки с суммой чисел.
def concatenate (x,y,z):
    x=str(x+y)+z
    return x
int1=int(input())
int2=int(input())
string=input()
print(concatenate(int1,int2,string))
# Реализуйте функцию рисующую на экране прямоугольник из звездочек
# «*». Ее параметрами будут целые числа, которые описывают длину и
# ширину такого прямоугольника
def rectangle (height,width):
    for i in range(height):
        for j in range(width):
            print("*",end=" ")
        print()
height=int(input())
width=int(input())
rectangle(height,width)
# Напишите функцию, которая реализует линейный поиск элемента в
# списке целых чисел. Если такой элемент в списке есть, то верните его
# индекс, если нет, то верните число «-1».
def find_element(list):
    if n in list:
        print("element in list,his index",list.index(n))
    else:
        print("-1")
        return
list=[random.randint(1,50) for _ in range(20)]
n=int(input())
#examination
print(list)
print(n)
find_element(list)
#Напишите функцию, которая вернет количество слов в строке текста.
def count (str):
    str=str.split()
    count=len(str)
    for element in str:
        if len(element)< 2:
            count-=1
    return count
n=input()
print(count(n))
# Число-палиндром с обеих сторон (справа налево и слева направо)
# читается одинаково. Самое большое число-палиндром, полученное
# умножением двух двузначных чисел: 9009 = 91 × 99. Найдите самый
# большой палиндром, полученный умножением двух трехзначных чисел.
# Выведите значение этого палиндрома и то, произведением каких чисел он
# является
max_value = 0
for element in range(999, 100, -1):
    for item in range(999, 100, -1):
        multiply = item * element
        if multiply > max_value:
            multiply = str(multiply)
            str1 = len(multiply) // 2
            s2 = multiply[::-1]
            if multiply[:str1] == s2[:str1]:
                value1=item
                value2=element
                max_value = int(multiply)
            else:
                continue
        else:
            break
print(value1,"*",value2,"=",max_value)
# Существуют такие последовательности чисел:
# 0,2,4,6,8,10,12
# 1,4,7,10,13
# 1,2,4,8,16,32
# 1,3,9,27
# 1,4,9,16,25
# 1,8,27,64,125
# Реализуйте программу, которая выведет следующий член этой
# последовательности (либо подобной им) на экран. Последовательность
# пользователь вводит с клавиатуры в виде строки. Например, пользователь
# вводит строку 0,5,10,15,20,25 и ответом программы должно быть число 30.
import math
n=list(map(int,input().split(",")))
q,q1,q2=(0,0,0)
degree2=2
degree3=3
while q!=n[0]:
    q+=1
while q1!=n[1]:
    q1+=1
while q2!=n[2]:
    q2+=1
if q2-q1==q1-q:
    Q=q1-q
    n.append(n[-1]+Q)
elif q2**0.5==q1:
    #случай квадратичной прогресии
    n.append(q1**(len(n)))
elif n[1]==2**degree2 and n[2]==3**degree2 :
    #квадраты чисел
    k=n[-1]**0.5
    k=int(k+1)
    n.append(k**2)
elif n[1]==2**degree3 and n[2]==3**degree3 :
    #кубы чисел
    k=n[-1]**(1/3)
    k=int(k+1)
    n.append(k**3)
print(n)
