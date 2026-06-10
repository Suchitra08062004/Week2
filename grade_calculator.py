# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures


student_results=[]

print("=" * 50)
print("      STUDENT GRADE CALCULATOR")
print("=" * 50)

# how many students to process
no_of_students=int(input("how many students to process:"))
while no_of_students<0:
    print("Input should be a positive integer")
    no_of_students=int(input("how many students to process:"))
    
#student name and marks for 3 subjects
student_names = []
student_marks = []

for i in range(no_of_students):
    print(f"\n=== STUDENT {i+1} ===")
    name=input("Enter your name:")
    while name=="":
        print("Name cannot be empty!")
        name=input("Enter your name:")
    student_names.append(name)
    print("Enter marks (0-100)")
    Math=int(input("Enter your maths marks: "))
    while Math<0 or Math>100:
        print("Enter marks between 0-100")
        Math=int(input("Enter your maths marks: "))
    Science=int(input("Enter your science marks: "))
    while Science<0 or Science>100:
        print("Enter marks between 0-100")
        Science=int(input("Enter your maths marks: "))
    English=int(input("Enter your english marks: "))
    while English<0 or English>100:
        print("Enter marks between 0-100")
        English=int(input("Enter your maths marks: "))
    student_marks.append([Math,Science,English])

#calculating average
average_list = []
for i in range(len(student_names)):
    average = round(sum(student_marks[i]) / len(student_marks[i]),2)
    average_list.append(average)
    
#assigning grades
def grade(average):
    if average>=90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', 'Very Good! You\'re doing well.'
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'
student_grades=grade(average_list[i])

#storing results 
for i in range(len(student_names)):
    grade_letter, comment = grade(average_list[i])

    student_results.append([
        student_names[i],
        average_list[i],
        grade_letter,
        comment
    ])

#results
print("\n" + "=" * 50)
print("            RESULTS SUMMARY")
print("=" * 50)
print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
print("-" * 60)

for result in student_results:
    print(f"{result[0]:<20} | {result[1]:>6.2f} | {result[2]:^5} | {result[3]}")
 
#class statistics   
print("\n" + "=" * 50)
print("          CLASS STATISTICS")
print("=" * 50)

class_average = round(sum(average_list) / len(average_list), 1)

highest_average = max(average_list)
highest_student = student_names[average_list.index(highest_average)]

lowest_average = min(average_list)
lowest_student = student_names[average_list.index(lowest_average)]

print(f"Total Students: {len(student_names)}")
print(f"Class Average: {class_average}")
print(f"Highest Average: {highest_average} ({highest_student})")
print(f"Lowest Average: {lowest_average} ({lowest_student})")
    
print("\n" + "=" * 50)
print("Thank you for using the Grade Calculator!")
print("=" * 50)
    
    
    
#search for student
search_name = input("Enter student name to search: ")

found = False

for result in student_results:
    if result[0].lower() == search_name.lower():
        print("\nStudent Found:")
        print(f"Name: {result[0]}")
        print(f"Average: {result[1]}")
        print(f"Grade: {result[2]}")
        print(f"Comment: {result[3]}")
        found = True
        break

if not found:
    print("Student not found.")
    
#saving results to file
with open("student_results.txt", "w") as file:
    file.write("STUDENT RESULTS\n")
    file.write("=" * 60 + "\n")

    for result in student_results:
        file.write(
            f"{result[0]} | {result[1]:.2f} | "
            f"{result[2]} | {result[3]}\n"
        )

print("Results saved successfully!")
    