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








numbers=[1,2,3,4,5]
print(numbers)


#slicing

numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

print("\n")

#Concatenation

list1 = [1, 2]
list2 = [3, 4]

result = list1 + list2
print(result)

print("\n")


fruits = ["Apple", "Banana", "Mango"]

print("Applee" in fruits)
print("Orange" not in fruits)


 # Updating list 

fruits = ["Apple", "Banana", "Mango"]

fruits[1]= "grapes"
print(fruits)




#delet list

num= [1,2,3,4,5,6,7]
del num[3]
print(num)





num= [1,2,3,4,5,6,7]
for n in num:
    print(n)





# All tuples and dictionary code:

# 1. Create Tuple

numbers = (10,20,30)

print(numbers)





# 2. Single Element Tuple

num = (10,)
print(type(num))



# 3. Indexing

numbers = (10,20,30)

print(numbers[1])
print(numbers[-1])

# 4. Slicing

number = ("mayur", "vinit", "vatsal")
print(number[0:2])


# 5. Concatenation

tuple1 = (1,2)
tuple2 = (3,4)

result = tuple1 + tuple2

print(result)

# 6. comparison

print((1,2)==(1,2))
print((1,2)!=(2,3))


students= ("Mayur", 20, "surat")
name, age, city = students
print(name)
print(age)
print(city)


#Count Example
grades = ("A", "B", "A", "C", "B", "A", "D", "A", "B", "C")

grade_a= grades.count("A")
grade_b= grades.count("B")
grade_c= grades.count("c")
grade_d= grades.count("D")

print("A: ", grade_a)
print("B: ", grade_b)
print("C: ", grade_c)
print("D: ", grade_d)



# Index Example:

String = ("mayur", "vinit", "vatsal", "parth")

text = "parth"
result = String.index(text)
print(result)


# dictionary code

# all operation with example:

# 1. Create Dictionary

details ={"name":"Mayur", "age":20, "city":"surat"}
print(details)


# 2. Access Value (Using Key)
students ={"name":"Mayur", "age":20, "city":"surat"}

print(students["name"])


# 3. Access Value using get()

students ={"name":"Mayur", "age":20, "city":"surat"}
print(students.get("age"))
print(students.get("enroll", "not found"))


# 4. Add a New Key-Value Pair

students ={"name":"Mayur", "age":20, "city":"surat"}

students["fruit"]="mango"
print(students)

# 5. Update an Existing Value

students ={"name":"Mayur", "age":20, "city":"surat"}
students["age"]=21
print(students)



# 6. Delete a Key-Value Pair (del)

students ={"name":"Mayur", "age":20, "city":"surat"}
del students["city"]
print(students)

# 7. pop item()


students ={"name":"Mayur", "age":20, "city":"surat"}

result= students.popitem()
print(result)
print(students)

# 8. setdefault()

students ={"name":"Mayur", "age":20, "city":"surat"}

result = students.setdefault("city", "surat")
print(result)
print(students)


# 9. update()

students ={"name":"Mayur", "age":20, "city":"surat"}
students.update({"name": "Unagar"})
print(students)



