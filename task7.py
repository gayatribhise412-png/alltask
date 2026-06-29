def get_grade(marks):
    if marks >= 90 and marks <= 100:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    elif marks >= 0:
        return "F"
    else:
        return "Invalid marks"

# Input
marks = float(input("Enter student marks out of 100: "))

# Function call
grade = get_grade(marks)

# Output
print(f"Marks: {marks}")
print(f"Grade: {grade}")
