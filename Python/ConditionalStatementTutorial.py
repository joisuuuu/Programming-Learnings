"""Conditional Statements and Collections"""
# employee = ["Joyce", "Adam", "Migz"]
#
# if "Joyce" in employee or "Adam" in employee:
#     print(True)
# else:
#     print(False)

fltGrade1 = float(input("Enter Grade 1: "))
fltGrade2 = float(input("Enter Grade 2: "))
fltGrade3 = float(input("Enter Grade 3: "))

fltAverage = (fltGrade1 + fltGrade2 + fltGrade3) / 3

print("Average Grade is: " + str(fltAverage))

if 98 <= fltAverage <= 100: # In C#, same with: fltAverage >= 98 and fltAverage <= 100
    print("With Highest Honor")
elif 95 <= fltAverage <= 97:
    print("With High Honor")
elif 90 <= fltAverage <= 94:
    print("With High Honor")
elif 75 <= fltAverage <= 89:
    print("With High Honor")
elif 51 <= fltAverage <= 74:
    print("Failed")
else:
    print("Invalid Grade")