import json
Student_data = []

# take student data from user
name = input("Enter student name:")
marks = int(input("Enter student marks:"))

new_student = {"name" : name, "marks" : marks}
Student_data.append(new_student)

#saving the data to JSON file
with open("Student_data.json","w") as file:
    json.dump(Student_data, file,indent = 4)

#read the existing data from json file
with open("Student_data.json","r") as file:
    students = json.load(file)

#Filter student data as marks > 50
print("Students with marks > 50:\n")

for s in students:
    if s["marks"] > 50:
        print(f"Name: {s['name']},Marks: {s['marks']}")
        