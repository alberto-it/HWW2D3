"""
Lesson 3: Assignments | Python Lists
1. Python List Transformation
Task 1: Given the list of grades:
"""
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
"""
Sort the grades in descending order and display the sorted list.
"""
grades.sort()
print("\nSorted grades:", grades)
"""
Task 2: Calculate the average grade and display it.
"""
print("Average Grade is", sum(grades)/len(grades))
"""
Task 3: Replace any grade below 80 with the value Failed.
"""
for i in range(len(grades)):
    if grades[i] < 80:
        grades[i] = "Failed"
    else: #Since the list is sorted, we don't need to keep checking
        break 
print(grades)
print()
"""
2. Advanced List Methods and Identity Operators
Task 1: Given the two lists:
"""
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
"""
Find out which students both submitted their assignments and attended the class.
"""
for student in submitted:
    if student in attended:
            print(student)
"""
Task 2: Check if the two lists are identical in terms of their content, regardless of order.
"""
print("Are lists identical?", "Yes" if submitted.sort == attended.sort else "No")
"""
Task 3: Using list methods, remove any student from the attended list who did not submit their assignment.
"""
for student in attended:
    if student not in submitted:
        attended.remove(student)
print("Updated 'attended' list:", attended, "\n")
"""
3. Advanced Slicing Techniques
Task 1: Given the list of temperatures:
"""
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
"""
Extract the temperatures for the second week (7 days) of the month. Expected Outcome: 83, 85, 86, 87, 88, 89, 90,
"""
print(temperatures[7:14])
"""
# Task 2: Extract all the temperatures above 100.
"""
print(temperatures[23:])
"""
Task 3: Reverse the list and extract temperatures from the 5th to the 10th day of the reversed list.
"""
print(temperatures[len(temperatures)-5:len(temperatures)-10-1:-1])
print()
"""
# 4. Deep Dive into Python Lists
# Task 1: Given the lists:
"""
students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]
"""
Filter out students who have grades below 80. Print the name, grade and activiy. Expected Outcome "Jane", 78, "Art"
"""
for i in range(len(students)):
     if grades[i] < 80:
          print('"' + students[i] + '", ' + str(grades[i]) + ', "' + activities[i] + '"')
print()
"""
Task 2: For the remaining students, add students name in a new list named students_approved. 
Expected Outcome: students_approved = ["John", "Doe", "Smith"]
"""
students_approved = []
for i in range(len(students)):
     if grades[i] >= 80:
          students_approved.append(students[i])
"""
Task 3: Print the list students_approved
"""
print(students_approved)
print()
