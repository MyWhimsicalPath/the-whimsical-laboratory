# Personal details below are fictional examples.
#Day 2: 30 Days of Python Programming

first_name = "Mira"

last_name = "Fernwick"

full_name = "Mira Fernwick"

print(first_name)
print(last_name)
print(full_name)

country = "Elderglen"
city = "Mossmere"
age = 28
year = 2026

print(country)
print(city)
print(age)
print(year) 

is_married = False
is_true = True
is_light_on = True

print(is_married)
print(is_true)
print(is_light_on)

specimen_name, petal_count, is_glowing = "Archive Bloom", 17, True

print(specimen_name)
print(petal_count)
print(is_glowing)

print("first_name", type(first_name))
print("age", type(age))
print("is_married", type(is_married))

print("last_name", type(last_name))
print("full_name", type(full_name))
print("country", type(country))
print("city", type(city))
print("year", type(year))
print("is_true", type(is_true))
print("is_light_on", type(is_light_on))
print("specimen_name", type(specimen_name))
print("petal_count", type(petal_count))
print("is_glowing", type(is_glowing))

print("First name length:", len(first_name))
print("Last name length:", len(last_name))

print("First name is shorter:", len(first_name) < len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
print("Total:", total)

diff = num_one - num_two
print("Diff:", diff)

product = num_one * num_two
print("Product:", product)

division = num_one / num_two
print("Division:", division)

remainder = num_two % num_one
print("Remainder:", remainder)

exp = num_one ** num_two
print("Exp:", exp)

floor_division = num_one // num_two
print("Floor division:", floor_division)

import math

radius = 30
area_of_circle = math.pi * radius ** 2

print("Area:", area_of_circle)

circum_of_circle = 2 * math.pi * radius

print("Circum:", circum_of_circle)

radius = float(input("Enter a radius in metres:"))
area_of_circle = math.pi *radius ** 2

print("Area in square metres:", area_of_circle)

first_name = input("What is your first name?")
last_name = input("What is your last name?")
country = input("What is your country?")
age = int(input("How old are you?"))

print("Name:", first_name, last_name)
print("Country:", country)
print("Age:", age)
print("Age type:", type(age))

help("keywords")
