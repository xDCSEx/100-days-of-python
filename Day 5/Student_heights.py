Student_heights = input().split()
for n in range(0, len(Student_heights)):
    Student_heights[n] = int(Student_heights[n])

print(Student_heights)

total_height = 0

for height in Student_heights:
    total_height += height

print(total_height)

print(f"total height = {total_height}")

number_of_students = 0

for students in Student_heights:
    number_of_students += 1

print(f"number of students = {number_of_students}")

avg_height = round(total_height / number_of_students)

print(f"average height = {avg_height}")