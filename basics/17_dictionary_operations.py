student = {
    "name": "Nitish",
    "course": "Integrated MSc Biology",
    "skill": "Python"
}

print("Student details:", student)

student["university"] = "University of Hyderabad"
print("After adding:", student)

student["skill"] = "Bioinformatics"
print("After updating skill:", student)

print("Student name:", student["name"])
print("Total details:", len(student))