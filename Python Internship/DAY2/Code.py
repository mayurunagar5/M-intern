from pydoc import text

# String Operations

name = "Mayur Unagar"
Field = "IT"
print(name[2])
print(name[1:5])
print(name[:])
print(name[:7])
print(name[0:9:2])

print(name+" "+Field)

print(Field * 3)

print("unagar" in name)

print(len(name))

print("Mayur" == "mayur")

for ch in name:
    print(ch)

#string all methods

text = "Python programming"

result = text.upper()

text = "PYTHON"
result = text.lower()
print(result)

# title()
text = "python programming"
result = text.title()
print(result)

# title()
text = "python programming"
result = text.capitalize()
print(result)

# swapcase()
text = "PyThOn"
result = text.swapcase()
print(result)

# strip()
text = "  Python  "
result = text.strip()
print(result)

# lstrip()
text = "   Python"
result = text.lstrip()
print(result)

# rstrip()
text = "Python   "
result = text.rstrip()
print(result)

# replace()
text = "I love Python"
result = text.replace("Python" , "Java")
print(result)

# split()
text = "Python Java C++"
result = text.split()
print(result)

# join()
languages = ["Python", "Java", "C++"]
result = "-".join(languages)
print(result)

# find()
text = "Python Programming"
result = text.find("Program")
print(result)

# index()
text = "Python Programming"
result = text.index("rogram")
print(result)

# count()
text = "programming"
result = text.count("m")
print(result)

# startswith()
text = "Python Programming"
result = text.startswith("Pthon")
print(result)

# endswith()
text = "Python Programming"
result = text.endswith("ing")
print(result)


# isalpha()
text = "Python"
result = text.isalpha()
print(result)

# isdigit()
text = "12345"
result = text.isdigit()
print(result)

# isalnum()
text = "Python123"
result = text.isdigit()
print(result)


# center()
text = "Python"
result = text.center(15)
print(result)


# ljust()
text = "Python"
result = text.ljust(15)
print(result)


# zfill()
text = "42"
result = text.zfill(5)
print(result)


# format()
result = "My name is {}".format("Mayur")
print(result)

# format()
result = "My name is {}".format("Mayur")
print(result)

# removeprefix() (Python 3.9+)
text = "unhappy"
result = text.removeprefix("un")
print(result)

# removesuffix() (Python 3.9+)
text = "filename.txt"
result = text.removesuffix(".txt")
print(result)


