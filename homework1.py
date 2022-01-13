# exercise_1 
# Write a Python-script that displays the message “Hello world”.
print("Hello world")
# exercise_2
# Rewrite the first script to display three any messages.
print("Привет,меня зовут Богдан.\nЭто моя первая программа.\nЯ хочу изучить Python")
# exercise_3
# Write a Python-script to reads values for the length and width of a 
# rectangle and returns the area of the rectangle.
a=int(input("1-я сторона(длинна):"))
b=int(input("2-я сторона(ширина):"))
area=a*b
print("площадь:",area)
# exercise_4
# Write a program that requests the user to enter two numbers and 
# prints the sum, product, difference and quotient of the two numbers.
print("Введите 2 числа")
x=int(input("число 1:"))
y=int(input("число 2:"))
print("sum:",x+y,"product:",x*y,"difference:",x-y,"quotionet:",x/y)
#exercise_5
#Write a program that reads in the radius of a circle and prints the 
#circle’s diameter, circumference and area. Use the constant value 3.14159 for π. 
#Do these calculations in output statements
r=int(input("Введите радиус окружности:"))
pi=int(3.14159)
print("Диаметр окружности:",2*r,"Длинна окружности:",2*pi*r,"Площадь:",pi*r*r)
