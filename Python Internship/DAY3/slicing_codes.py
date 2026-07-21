# 1. Basic Slicing

course_name = "DataScience"

print(course_name[0:4])     


# ==========================================
# 2. Omitting Start

city_name = "Ahmedabad"

print(city_name[:5])          


# ==========================================
# 3. Omitting Stop

company_name = "OpenAI"

print(company_name[2:])       


# ==========================================
# 4. Omitting Both (Copy Sequence)

language_name = "Python"

print(language_name[:])      


# ==========================================
# 5. Step

animal_name = "Elephant"

print(animal_name[::2])


# ==========================================
# 6. Reverse String

country_name = "India"

print(country_name[::-1])    

# ==========================================
# 7. Negative Index

movie_title = "Interstellar"

print(movie_title[-5:])       


# ==========================================
# 8. Negative Step

planet_name = "Jupiter"

print(planet_name[::-2])    


# ==========================================
# 9. String Slicing

full_name = "Mayur Unagar"

print(full_name[:5])          


# ==========================================
# 10. List Slicing

student_marks = [85, 90, 78, 92, 88, 95]

print(student_marks[1:5])    

# ==========================================
# 11. Tuple Slicing

week_days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

print(week_days[2:6])         


# ==========================================
# 12. Range Slicing

number_series = range(10, 31)

print(list(number_series[5:10]))   


# ==========================================
# 13. Nested List Slicing

student_data = [
    ["Mayur", 20],
    ["Rahul", 22],
    ["Amit", 21],
    ["Karan", 23]
]

print(student_data[:2])

# Output:
# [['Mayur', 20], ['Rahul', 22]]


# ==========================================
# 14. Set (Slicing Not Supported)

prime_numbers = {2, 3, 5, 7, 11}

# print(prime_numbers[1:3])




# ==========================================
# 15. Dictionary (Direct Slicing Not Supported)

employee_info = {
    "id": 101,
    "name": "Mayur",
    "department": "AI",
    "salary": 50000
}

# print(employee_info[0:2])




# ==========================================
# 16. Dictionary Keys Slicing

book_details = {
    "title": "Python",
    "author": "Guido",
    "price": 999,
    "pages": 550
}

print(list(book_details.keys())[:2])




# ==========================================
# 17. Dictionary Values Slicing

car_details = {
    "brand": "Tesla",
    "model": "Model Y",
    "year": 2025,
    "color": "White"
}

print(list(car_details.values())[:2])




# ==========================================
# 18. Dictionary Items Slicing

mobile_specs = {
    "brand": "Apple",
    "model": "iPhone 16",
    "storage": "256GB",
    "price": 95000
}

print(list(mobile_specs.items())[:2])




# ==========================================
# 19. Last 4 Digits of Phone Number

contact_number = "9876543210"

print(contact_number[-4:])      


# ==========================================
# 20. File Extension

document_name = "assignment.pdf"

print(document_name[-3:])    


# ==========================================
# 21. Username from Email

email_address = "mayur.unagar@gmail.com"

print(email_address[:email_address.index("@")])




# ==========================================
# 22. Domain from Email

official_email = "student@college.edu"

print(official_email[official_email.index("@")+1:])




# ==========================================
# 23. Last 5 Transactions

monthly_transactions = [250, 600, 1200, 450, 980, 1500, 320, 700]

print(monthly_transactions[-5:])

