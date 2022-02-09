# Напишите программу, которая сгенерирует два списка. Один с числами
# кратными 3, другой с числами кратными 5. С помощью множеств
# создайте список с числами, которые есть в обоих множествах
list1 = []
for element in range(3, 100, 3):
    list1.append(element)
set_1 = set(list1)
list2 = []
for element in range(5, 100, 5):
    list2.append(element)
set_2 = set(list2)
set_3 = set_1.intersection(set_2)
print(set_3)
# Напишите программу, которая считает две строки текста с клавиатуры и
# выведет на экран буквы, которые есть одновременно и в первой, и во
# второй строке. Например, для строк «Hello» и «World» на экране должны
# быть буквы «l» и «o».
s1 = input()
s2 = input()
set_1 = set(s1)
set_2 = set(s2)
set_3 = set_1 & set_2
print(set_3)
# +доработал перевод римских цифр в обычные
dict = {"X": 10, "I": 1, "IV": 4, "V": 5, "IX": 9, "XL": 40, "XLI": 41, "XLII": 42, "XLIII": 43, "XLIV": 44, "XLV": 44,
        "XLVI": 46,
        "XLVII": 47, "XLVIII": 48, "XLIX": 47, "L": 50, "XC": 90, "C": 100}
n = input()
if n in dict:
    print(dict[n])
else:
    translate = 0
    for key in (dict):
        for item in (n):
            if key == item:
                item = dict.get(key)
                translate += item
item1 = ""
item2 = ""
for item in n:
    if item1 + item == "IV" or item2 + item == "IX":
        translate -= 2
    item1 = item2 = item
print(translate)
