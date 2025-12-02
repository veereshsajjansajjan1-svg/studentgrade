# Student Grade Evaluation Program

# Accept marks of 5 subjects
marks = []
for i in range(1, 6):
    score = float(input(f"Enter marks for subject {i}: "))
    marks.append(score)

# Calculate average
average = sum(marks) / 5
print("\nAverage Marks:", average)

# Determine grade
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Grade:", grade)
