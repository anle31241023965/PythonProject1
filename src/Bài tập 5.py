# Set
# 1.Write a Python program to find the maximum and minimum values in a set.
numbers = {10, 5, 25, 3, 15}
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# 2.Write a Python program to check if a given value is present in a set or not.
value = 15
if value in numbers:
    print(value, "is present in the set")
else:
    print(value, "is NOT present in the set")

# 3.Write a Python program to check if two given sets have no elements in common.
set1 = {1, 2, 3, 4}
set2 = {5, 6, 7}
if set1.isdisjoint(set2):
    print("No elements in common")
else:
    print("They have common elements")

# 4.Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
unique_words = set(words)
print("Unique words:", unique_words)

word_count = {word: words.count(word) for word in unique_words}
print("Word frequency:", word_count)

# 5.Given two sets of numbers, write a Python program to find the missing numbers in the second set as compared to the first and vice versa. Use the Python set.
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}

missing_in_B = setA - setB
missing_in_A = setB - setA

print("Missing in B compared to A:", missing_in_B)
print("Missing in A compared to B:", missing_in_A)

#
# Dictionary
# Restructuring the company data: Suppose you have a dictionary that contains information about employees at a company. Each employee is identified by an ID number, and their information includes their name, department, and salary. You want to create a nested dictionary that groups employees by department so that you can easily see the names and salaries of all employees in each department.
#
# Write a Python program that when given a dictionary, employees, outputs a nested dictionary, dept_employees, which groups employees by department.

employees = {
    1001: {"name": "Alice", "department": "Engineering", "salary": 75000},
    1002: {"name": "Bob", "department": "Sales", "salary": 50000},
    1003: {"name": "Charlie", "department": "Engineering", "salary": 80000},
    1004: {"name": "Dave", "department": "Marketing", "salary": 60000},
    1005: {"name": "Eve", "department": "Sales", "salary": 55000}
}
dept_employees = {}

for emp_id, info in employees.items():
    dept = info["department"]
    if dept not in dept_employees:
        dept_employees[dept] = {}
    dept_employees[dept][emp_id] = {
        "name": info["name"],
        "salary": info["salary"]
    }

print(dept_employees)