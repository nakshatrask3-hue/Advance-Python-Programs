
import csv
import json

# Storing student details in CSV file
students = [
    [101, "Rahul", "CSE", 85, 90, 80],
    [102, "Priya", "IT", 75, 80, 85],
    [103, "Amit", "AIML", 60, 65, 70]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Roll_No", "Name", "Branch",
                     "Subject1", "Subject2", "Subject3"])

    writer.writerows(students)

# Reading CSV file and processing records
processed_students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        m1 = int(student["Subject1"])
        m2 = int(student["Subject2"])
        m3 = int(student["Subject3"])

        total = m1 + m2 + m3
        percentage = total / 3

        if percentage >= 90:
            grade = "A"
        elif percentage >= 75:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"

        student["Total"] = total
        student["Percentage"] = round(percentage, 2)
        student["Grade"] = grade

        processed_students.append(student)

# Storing processed records in JSON file
with open("students.json", "w") as file:
    json.dump(processed_students, file, indent=4)

print("Student records processed successfully!")

# Displaying results
for student in processed_students:
    print("\nRoll Number:", student["Roll_No"])
    print("Name:", student["Name"])
    print("Branch:", student["Branch"])
    print("Total Marks:", student["Total"])
    print("Percentage:", student["Percentage"], "%")
    print("Grade:", student["Grade"])
