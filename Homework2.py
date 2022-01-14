# Construct an integer from the string "123"
a = int("123")
print(type(a), "\n""-------")  # int
# Construct an integer from the string "123
a1 = float(123)
print(type(a1), a1, "\n""-------")  # float, 123.0
# Construct an integer from the float 12.345
a2 = int(12.345)
print(a2, "\n""-------")
# Write a Python-script that detects the last 4 digits of a credit card
print("enter card details without spaces")
script = int(input("Input number of credit card(16 numbers):"))
numbers = script % 10 ** 4
print("Last 4 numbers of credit card:", numbers, "\n""-------")
# another solution (if the user enters data separated by a space)
s = input("Input number of credit card(16 numbers):")
s1 = s[14:]
print("Last 4 numbers of credit card:", s1, "\n""-------")
# Write a Python-script that calculates the sum of #the digits of a three-digit number
x = int(input("enter a three-digit number:"))
x1 = x // 100
x2 = x // 10 % 10
x3 = x % 10
print(x1, x2, x3)
sum = (x1 + x2 + x3)
print("Sum of three-digit number", sum,"\n""-------")
# Write a program that calculates and displays the area of a triangle if its sides
# are known
A = int(input("enter a value of a side:"))
B = int(input("enter a value of b side:"))
C = int(input("enter a value of c side:"))
# To find square of triangle need a semi-perimeter
p = (A + B + C) / 2
s = (p * (p - A) * (p - B) * (p - C)) ** (1 / 2)
print("Square is", s, "\n""-------")
# Write a Python-script that calculates the sum of the digits of a number
b = int(input("enter a digit: "))
b1 = b // 10000000000 % 10
b2 = b // 1000000000 % 10
b3 = b // 100000000 % 10
b4 = b // 10000000 % 10
b5 = b // 1000000 % 10
b6 = b // 100000 % 10
b7 = b // 10000 % 10
b8 = b // 1000 % 10
b9 = b // 100 % 10
b10 = b % 100 // 10
b11 = b % 10
sum2 = (b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11)
print(sum2, "\n""-------")
# *Determine the number of digits in a number
n = (input("enter a number: "))
digit = len(n)
print(digit, "\n""-------")
# Print the digits in reverse order
n = "7812341"
n1 = n[-1]
n2 = n[-2]
n3 = n[-3]
n4 = n[-4]
n5 = n[-5]
n6 = n[-6]
print(n1, n2, n3, n4, n5, n6)
