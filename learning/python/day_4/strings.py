# Day 4: Strings

challenge = "Thirty" + " " + "Days" + " " + "Of" + " " + "Python"
print(challenge)

company = "Coding" + " " + "For" + " " + "All"
print(company)
print(len(company))

print(company.upper())
print(company.lower())
print(company)

print(company.capitalize())
print(company.title())
print(company.swapcase())

print(company[0:6])
print(company[7:])

print("Coding" in company)
print(company.find("Coding"))

print(company.replace("Coding", "Python"))

sentence = "Python" + " " + "for" + " " + "Everyone"

print(sentence.replace("Everyone", "All"))

print(company.split())

companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"

print(companies.split(", "))

print("First character:", company[0])
print("Last index:", len(company) - 1)
print("Character at index 10:", company[10])

phrase = "Python For Everyone"
words = phrase.split()

abbreviation = words[0][0] + words[1][0] + words[2][0]
print(abbreviation)

company_words = company.split()

company_abbreviation = company_words[0][0] + company_words[1][0] + company_words[2][0]
print(company_abbreviation)

print("Position of C:", company.index("C"))
print("Position of F:", company.index("F"))


message = "Coding For All People"

print("First l", message.find("l"))
print("Last l:", message.rfind("l"))

sentence = "You cannot end a sentence with because because because is a conjunction"

print("First because:", sentence.find("because"))
print("Last because:", sentence.rindex("because"))
print(sentence[31:54])

start = sentence.find("because")
end = sentence.rindex("because") + len("because")
print(sentence[start:end])

print("Starts with Coding?", company.startswith("Coding"))
print("Ends with coding?", company.endswith("coding"))

messy_company = "   Coding For All      "
clean_company = messy_company.strip()
print("Before:", repr(messy_company))
print("After:", repr(clean_company))

print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]

joined_libraries = "# ".join(libraries)
print(joined_libraries)

print("I am enjoying this challenge.\nI just wonder what is next.")

print("Name\tAge\tCountry\t\tCity")
print("Mira\t28\tElderglen\tMossmere")

radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area:g} square metres.")

a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")

