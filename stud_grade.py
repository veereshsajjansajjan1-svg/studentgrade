

marks = [80, 75, 90, 60, 85]   # fixed sample marks

average = sum(marks) / 5

print("Average Marks:", average)

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
