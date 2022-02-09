# Напишите программу, которая сгенерирует два списка. Один с числами
# кратными 3, другой с числами кратными 5. С помощью множеств
# создайте список с числами, которые есть в обоих множествах
list1=[]
for element in range(3,100,3):
    list1.append(element)
set_1=set(list1)
list2=[]
for element in range(5,100,5):
    list2.append(element)
set_2=set(list2)
set_3=set_1.intersection(set_2)
print(set_3)