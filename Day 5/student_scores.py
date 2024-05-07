student_scores = input().split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

highest_score = 0

print(student_scores)

for highest in student_scores:
    if highest_score < highest:
        highest_score = highest

print(f"The highest score in the class is {highest_score}")