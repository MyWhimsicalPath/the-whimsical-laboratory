# Day 3: Operators
# Age and height below are fictional examples.

age = 28
height = 1.72
complex_number = 2 + 3j

print("Age", age, type(age))
print("Height:", height, type(height))
print("Complex number:", complex_number, type(complex_number))


base = float(input("Enter the triangle base:"))
triangle_height = float(input("Enter the triangle height:"))

area = 0.5 * base * triangle_height

print("The area of the triangle is:", area)

a = float(input("Enter side a:"))
b = float(input("Enter side b:"))
c = float(input("Enter side c:"))

perimeter = a + b + c

print("The perimeter of the triangle is:", perimeter)


length = float(input("Enter the rectangle length:"))
width = float(input("Enter the rectangle width:"))

rectangle_area = length * width
rectangle_perimeter = 2 * (length + width)

print("Rectangle's area:", rectangle_area)
print("Rectangle's perimeter:", rectangle_perimeter)


import math

radius = float(input("Enter the circle radius:"))

circle_area = math.pi * radius ** 2

print("Circle's area:", circle_area)

circumference = 2 * math.pi * radius

print("Circle's circumference:", circumference)


m = 2
b = -2

slope = m
y_intercept = b
x_intercept = -b /m

print("Slope:", slope)
print("Y-intercept:", y_intercept)
print("X-intercept:", x_intercept)


x1, y1 = 2, 2
x2, y2 = 6, 10

slope_two = (y2 - y1) / (x2 - x1)

distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("Slope two:", slope_two)
print("Distance:", distance)

print("Are the slopes equal?", slope == slope_two)

x = 0
y = x**2 + 6 * x + 9

print("x", x)
print("y", y)

x = -1
y = x**2 + 6 * x + 9

print("x", x)
print("y", y)

x = -2
y = x**2 + 6 * x + 9

print("x", x)
print("y", y)

x = -3
y = x**2 + 6 * x + 9

print("x", x)
print("y", y)


python_length = len("python")
dragon_length = len("dragon")

print("Python length:", python_length)
print("Dragon length:", dragon_length)

print(python_length != dragon_length)

print("on" in "python" and "on" in "dragon")


sentence = "I hope this course is not full of jargon"

print("jargon" in sentence)


print("on" not in "dragon" and "on" not in "python")


word_length = len("python")
length_float = float(word_length)
length_string = str(length_float)

print(word_length, type(word_length))
print(length_float, type(length_float))
print(length_string, type(length_string))


number = int(input("Enter a whole number:"))
is_even = number % 2 == 0

print("Is the number even?", is_even)

print("Floor division:", 7 // 3)
print("Converted integer:", int(2.7))
print("Are they equal?", 7 // 3 == int(2.7))

print("Type of quoted 10:", type("10"))
print("Type of unquoted 10:", type(10))

print("Are they the same kind of data?", type("10") == type(10))



# int("9.8") raises ValueError; convert to float first.
decimal_number = float("9.8")
whole_number = int(decimal_number)

print("Converted number:", whole_number)
print("Is it equal to 10?", whole_number == 10)


hours = float(input("Hours worked:"))
rate_per_hour = float(input("Pay per hour:"))

weekly_earnings = hours * rate_per_hour

print("Weekly earning:", weekly_earnings)


years = int(input("Enter the number of years:"))

# This exercise assumes 365 days per year, ignoring leap years.
seconds_lived = years * 365 * 24 * 60 * 60

print("Seconds lived:", seconds_lived)



n = 1
print(n, n**0, n**1, n**2, n**3)

n = 2
print(n, n**0, n**1, n**2, n**3)

n = 3
print(n, n**0, n**1, n**2, n**3)

n = 4
print(n, n**0, n**1, n**2, n**3)

n = 5
print(n, n**0, n**1, n**2, n**3)


