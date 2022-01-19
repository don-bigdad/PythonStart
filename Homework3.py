# Write a Python program to print the number entered by user only if the
# number entered is negative.
a = int(input("enter a number"))
if a < 0:
    print(a)
else:
    print("You entered a positive number")
# Write a Python program to check if the value a is less than 20 or not.
A = int(input("Enter a value of A"))
if A > 20:
    print("A>20, A=", A)
else:
    print("A<=20", A)
# Write a Python program to check if W given number is Zero or Not.
W = int(input("Enter a number:"))
if W == 0:
    print("W is zero")
else:
    print("W is now zero")
# Write a Python program to check if a given number is Even or Odd
number = int(input("Enter a number:"))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")
# Write a Python program to find largest number among three numbers
# entered by user
x = int(input())
y = int(input())
z = int(input())
q = max(x, y, z)
print(q)
# Determine the number of days in the year that the user enters.
year = int(input("Enter a year:"))
if year % 4 == 0 and year % 400 == 0 or year % 100 != 0:
    print("Year is leap", year)
else:
    print("Year is not leap")
# Exist of triangle
a = float(input())
b = float(input())
c = float(input())
if a + b > c and a + c > b and b + c > a:
    print("triangle is exist")
else:
    print("triangle doesn`t exist")
# Task about house
apartament = int(input("enter the apartament:"))
if apartament <= 36:
    n = 1
    print("1 entrance")
elif apartament <= 72:
    n = 2
    print("2 entrance")
elif apartament <= 108:
    n = 3
    print("3 entrance")
elif apartament <= 144:
    n = 5
    print("4 entrance")
else:
    print("there is no such apartment in the house")
floor = (apartament - 1) // 4 + 1
print("Квартира находится на", floor, "этаже", n, "подьезда")
