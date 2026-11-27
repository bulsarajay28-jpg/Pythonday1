age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

if age >= 18 and marks >= 50:
    print("You are eligible for the exam.")
if age <18 or marks < 50:
    print("You meet one of the criteria for the exam.")
else:
    print("You are not eligible for the exam.")  