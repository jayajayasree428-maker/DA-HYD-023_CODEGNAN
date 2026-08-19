#Student Marks Manager
marks = []
for i in range(3):
    
    mark = int(input("Enter mark: "))
    marks.append(mark)
print("Original marks:", marks)
marks.insert(0, 90)
marks.extend([75, 85])
if 75 in marks:
    marks.remove(75)
removed_mark = marks.pop()
print("Removed mark:", removed_mark)
print("Final marks:", marks)
print("Number of marks:", len(marks))


#Number List
numbers = [20, 10, 30, 20, 40, 20]

numbers.sort()
print("Ascending order:", numbers)
numbers.reverse()
print("Descending order:", numbers)

number = int(input("Enter number: "))

if num in numbers:
    print("Count:", numbers.count(num))
    print("Index:", numbers.index(num))
else:
    print("Number not found")

print(min(numbers))
print(max(numbers))
print(sum(numbers))

#Even and odd

numbers = [10, 15, 20, 25, 30, 35]

even = []
odd = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print("Even numbers:", even)
print("Odd numbers:", odd)

#Slicing
print("First three:", numbers[:3])
print("Last three:", numbers[-3:])


numbers.clear()

print("Original list:", numbers)
print("Backup list:", backup)



#Unique name manager
names = ["Asha", "Rahul", "Asha", "John", "Rahul"]

students = set(names)

students.add("Meera")
students.update("Arun", "Priya")

if "John" in students:
    students.remove("John")

students.discard("David")

for student in students:
    print(student)


#Course student comparison
python_students = {"Asha", "Rahul", "John", "Meera"}
da_students = {"Rahul", "Meera", "Arun"}

both_courses = python_students.union(da_students)
both = python_students.intersection(da_students)

only_python = python_students.difference(da_students)
only_one = python_students.symmetric_difference(da_students)

is_subset = da_students.issubset(python_students)
is_superset = python_students.issuperset(da_students)
is_disjoint = python_students.isdisjoint(da_students)

print("Students in both courses:")
for student in both_courses:
    print(student)
print("\nStudents learning both Python and DA:")
for student in both:
    print(student)
print("\nStudents learning only Python:")
for student in only_python:
    print(student)
print("\nStudents learning only one course:")
for student in only_one_course:
if is_subset:
    print("\nDA students are a subset of Python students: True")
else:
    print("\nDA students are a subset of Python students: False")

if is_superset:
    print("Python students are a superset of DA students: True")
else:
    print("Python students are a superset of DA students: False")

if is_disjoint:
    print("The two sets are disjoint: True")
else:
    print("The two sets are disjoint: False")







