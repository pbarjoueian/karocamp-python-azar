from datetime import datetime

students = []
message = "Please enter your "

first_name = input(message + "first name:")
last_name = input(message + "last name:")
birth_year = int(input(message + "birth year:"))
gpa = float(input(message + "GPA"))

students.append(
    {
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
        "gpa": gpa,
    }
)

first_name = input(message + "first name:")
last_name = input(message + "last name:")
birth_year = int(input(message + "birth year:"))
gpa = float(input(message + "GPA"))

students.append(
    {
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
        "gpa": gpa,
    }
)

first_name = input(message + "first name:")
last_name = input(message + "last name:")
birth_year = int(input(message + "birth year:"))
gpa = float(input(message + "GPA"))

students.append(
    {
        "first_name": first_name,
        "last_name": last_name,
        "birth_year": birth_year,
        "gpa": gpa,
    }
)

current_year = datetime.now().year

full_name_1 = students[0]["first_name"] + " " + students[0]["last_name"]
print(full_name_1.upper())
print(current_year - students[0]["birth_year"])
full_name_2 = students[1]["first_name"] + " " + students[1]["last_name"]
print(full_name_2.upper())
print(current_year - students[1]["birth_year"])
full_name_3 = students[2]["first_name"] + " " + students[2]["last_name"]
print(full_name_3.upper())
print(current_year - students[2]["birth_year"])


gpas = []

gpas.append(students[0]["gpa"])
gpas.append(students[1]["gpa"])
gpas.append(students[2]["gpa"])

print(round(sum(gpas) / len(gpas), 2))
