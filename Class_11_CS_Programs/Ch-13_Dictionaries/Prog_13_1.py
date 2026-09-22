# Program 13.1: Create and traverse Dictionary
# KEYWORD EXPLANATION:
# {} - Dictionary literal mapping unique keys to values.
# dict.items() - Method returning key-value pairs as iterable tuples.

n = int(input("Enter number of students: "))
students = {}

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    marks = float(input(f"Enter marks for {name}: "))
    students[name] = marks

print("
Student Details:")
for name, marks in students.items():
    print(f"Student: {name} | Marks: {marks}")
