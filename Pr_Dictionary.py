student_data ={"Name": "Ganesh", "DOB": "31/07/1999", "Education":"Graduation", "Gender": "Male"}
print("Details of student is:",student_data)

# len:
print("Length of student_data is:",len(student_data))

# update:
student_data.update({"Address":"Jalgaon"})
print("After updating Address student_data is:",student_data)

# values:
print("Values in student_data are: ", student_data.values())

# keys:
print("Keys in student_data are: ", student_data.keys())

# items:
print("Items in student_data are: ", student_data.items())

# copy:
stud_copy = student_data.copy()
print("Copy of student_data is: ", stud_copy)

# pop:
print(student_data.pop("DOB"), "is poped from student_data.")

# popitem:
print(student_data.popitem(), ": This item is poped from student_data")

# clear:
student_data.clear()
print(student_data)



