# Используя словарь, напишите программу, которая выведет на экран
# название дня недели по его номеру. (1 - «Monday»)
week={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
n=int(input("input day of week"))
print(week[n])
# Представьте описание кота (домашнее животное) на основе словаря.
cat={
    "breed":"British",
    "age":4,
    "color":"white",
    "gender":"female"
}
# Напишите программу которая считает строку текста с клавиатуры и
# выведет на экран статистику, сколько раз какая буква встречается в
# этой строке. Например, для строки «Hello world» эта статистика
# выглядит, как: «H» - 1 , «e» - 1, «l» - 3 и т. д.
n=input()
for item in (n):
    print(n.count(item))
#все что смог не могу разобраться и вывести 14,24,,34,44...
dict={"X":10,"I":1,"IV":4,"V":5,"IX":9,"XL":40,"L":50,"XC":90,"C":100}
n=input()
print(n)
translate=0
for key in (dict):
    for item in (n):
        if key==item:
            item=dict.get(key)
            translate+=item
# if "IV" or "IX" in n:
#     translate-=1
print(translate)

